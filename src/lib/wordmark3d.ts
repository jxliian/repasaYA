/**
 * Wordmark "repasaYA" en 3D: geometría extruida desde el contorno real de
 * Unbounded (vía opentype.js) con acabado glossy tipo burbuja.
 *
 * Lo usan dos sitios —la pantalla de carga y el hero— con animaciones
 * distintas, así que aquí solo vive el montaje de Three.js. Quién lo hace
 * girar, y cómo, es cosa de cada componente.
 *
 * Devuelve `null` si no hay WebGL, si falla la fuente o si el navegador no
 * puede con los imports dinámicos: en ese caso quien llama deja visible su
 * propio texto en CSS.
 */

export interface WordmarkTransform {
  rotX?: number;
  rotY?: number;
  scale?: number;
}

export interface Wordmark {
  /** Coloca el grupo y pinta un fotograma. */
  render(t?: WordmarkTransform): void;
  /** Reajusta el lienzo y recoloca la cámara para que el texto quepa. */
  resize(width: number, height: number): void;
  dispose(): void;
}

export interface WordmarkOptions {
  /** Color del texto. Por defecto, blanco-lavanda tipo navbar. */
  color?: number;
  /** Color del punto. Por defecto, púrpura de marca. */
  dotColor?: number;
  /** Proporción del ancho del lienzo que ocupa el texto (0-1). */
  fill?: number;
}

export async function createWordmark(
  canvas: HTMLCanvasElement,
  fontUrl: string,
  { color = 0xeeecfb, dotColor = 0xa78bea, fill = 0.78 }: WordmarkOptions = {}
): Promise<Wordmark | null> {
  try {
    const THREE = await import('three');
    const { RoomEnvironment } = await import(
      'three/addons/environments/RoomEnvironment.js'
    );
    const opentype: any = await import('opentype.js');

    const parse = opentype.parse || opentype.default?.parse;
    const font = parse(await fetch(fontUrl).then((r) => r.arrayBuffer()));

    const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
    if (!renderer.getContext()) return null;
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(38, 1, 0.1, 100);
    camera.position.set(0, 0, 9);

    // El entorno de sala da los reflejos que hacen que parezca plástico
    // brillante en vez de un bloque de color plano.
    const pmrem = new THREE.PMREMGenerator(renderer);
    scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
    scene.add(new THREE.AmbientLight(0xffffff, 0.55));

    const key = new THREE.DirectionalLight(0xffffff, 1.25);
    key.position.set(3, 6, 7);
    scene.add(key);

    const rim = new THREE.DirectionalLight(0x8f6bff, 0.85);
    rim.position.set(-5, -2, 3);
    scene.add(rim);

    // Función auxiliar para convertir rutas de opentype.js a formas de Three.js
    function pathToShapes(pathObj: any) {
      const sp = new THREE.ShapePath();
      for (const c of pathObj.commands) {
        if (c.type === 'M') sp.moveTo(c.x, -c.y);
        else if (c.type === 'L') sp.lineTo(c.x, -c.y);
        else if (c.type === 'Q') sp.quadraticCurveTo(c.x1, -c.y1, c.x, -c.y);
        else if (c.type === 'C') sp.bezierCurveTo(c.x1, -c.y1, c.x2, -c.y2, c.x, -c.y);
      }
      return sp.toShapes(true);
    }

    // 1. Geometría del texto "repasaYA"
    const pathText = font.getPath('repasaYA', 0, 0, 1);
    const geoText = new THREE.ExtrudeGeometry(pathToShapes(pathText), {
      depth: 0.3,
      bevelEnabled: true,
      bevelThickness: 0.1,
      bevelSize: 0.062,
      bevelSegments: 8,
      curveSegments: 10,
    });
    geoText.computeBoundingBox();
    const textMaxX = geoText.boundingBox?.max.x ?? 4.5;

    // 2. Geometría del punto "." colocado justo a la derecha
    const pathDot = font.getPath('.', textMaxX + 0.08, 0, 1);
    const geoDot = new THREE.ExtrudeGeometry(pathToShapes(pathDot), {
      depth: 0.3,
      bevelEnabled: true,
      bevelThickness: 0.1,
      bevelSize: 0.062,
      bevelSegments: 8,
      curveSegments: 10,
    });

    // Materiales: texto blanco lavanda como navbar + punto púrpura con emissive neón
    const matText = new THREE.MeshPhysicalMaterial({
      color,
      metalness: 0.02,
      roughness: 0.1,
      clearcoat: 1,
      clearcoatRoughness: 0.05,
      envMapIntensity: 1.5,
    });

    const matDot = new THREE.MeshPhysicalMaterial({
      color: dotColor,
      emissive: 0x7c5cff,
      emissiveIntensity: 0.8,
      metalness: 0.05,
      roughness: 0.1,
      clearcoat: 1,
      clearcoatRoughness: 0.05,
      envMapIntensity: 2.0,
      transparent: true,
      opacity: 1,
    });

    const group = new THREE.Group();
    const meshText = new THREE.Mesh(geoText, matText);
    const meshDot = new THREE.Mesh(geoDot, matDot);
    group.add(meshText);
    group.add(meshDot);

    // Centrar el grupo combinando texto + punto
    const box = new THREE.Box3().setFromObject(group);
    const center = new THREE.Vector3();
    box.getCenter(center);
    meshText.position.sub(center);
    meshDot.position.sub(center);

    scene.add(group);
    const wordWidth = box.max.x - box.min.x;

    return {
      resize(width, height) {
        if (width < 1 || height < 1) return;
        renderer.setSize(width, height, false);
        camera.aspect = width / height;
        // Aleja la cámara lo justo para que el conjunto ocupe `fill` del ancho
        const dist =
          wordWidth / fill / 2 / Math.tan(((camera.fov * Math.PI) / 180) / 2) / camera.aspect;
        camera.position.z = Math.max(4, dist);
        camera.updateProjectionMatrix();
      },

      render({ rotX = 0, rotY = 0, scale = 1 } = {}) {
        // Animación de pulso exactamente igual a la del navbar (dotPulse 2.4s)
        const t = performance.now() / 1000;
        const pulse = 0.35 + 0.65 * (0.5 + 0.5 * Math.sin((t * Math.PI * 2) / 2.4));
        matDot.emissiveIntensity = pulse * 0.95;
        matDot.opacity = pulse;

        group.rotation.x = rotX;
        group.rotation.y = rotY;
        group.scale.setScalar(scale);
        renderer.render(scene, camera);
      },

      dispose() {
        geoText.dispose();
        geoDot.dispose();
        matText.dispose();
        matDot.dispose();
        pmrem.dispose();
        renderer.dispose();
      },
    };
  } catch (e) {
    return null;
  }
}
