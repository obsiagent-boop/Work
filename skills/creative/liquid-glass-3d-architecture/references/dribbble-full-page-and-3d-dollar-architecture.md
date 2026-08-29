# Dribbble Full-Page Reverse-Engineering & 3D WebGL Dollar Architecture

## 1. Full-Page Dribbble Emulation Mandate
When emulating top-trending Dribbble / Awwwards design paradigms (such as Anatoliy Demyanchuk, OpenSim, or Priceless):
- **Full Architecture Emulation:** Never restrict delivery to a minimal component snippet or isolated widget. Recreate the complete page layout:
  - Bracketed split-hero navigation (`[About]`, `[Asset Selection]`, `[Service Type]`)
  - Circular telemetry ray diagrams and vector geometries
  - Parabolic dashed milestone curves (`M1`, `M2`, `M3`, `M4`) connecting roadmap cards
  - High-contrast spatial dark and cream themes with zero voids
- **Purified Branding:** Strip all third-party showcase names (e.g. "OpenSim", "Intelliphy") and brand exclusively for the target project (e.g. `qnt.`).

---

## 2. 3D Real Sovereign Dollar Bullion Mesh Specification
```javascript
// High-Relief 24k Gold Alloy Sovereign Dollar Coin
const goldMat = new THREE.MeshStandardMaterial({
  color: 0xF59E0B,
  metalness: 0.96,
  roughness: 0.12,
  emissive: 0x78350F,
  emissiveIntensity: 0.2
});

const goldReliefMat = new THREE.MeshStandardMaterial({
  color: 0xFCD34D,
  metalness: 0.98,
  roughness: 0.08
});

// Coin Cylinder Base
const coin = new THREE.Mesh(new THREE.CylinderGeometry(4.2, 4.2, 0.6, 64), goldMat);
coin.rotation.x = Math.PI * 0.5;

// Double-Sided High-Relief Dollar Symbol ($)
function createDollarMesh() {
  const dGroup = new THREE.Group();
  const topArc = new THREE.Mesh(new THREE.TorusGeometry(1.2, 0.28, 16, 32, Math.PI * 1.3), goldReliefMat);
  topArc.position.set(0, 1.0, 0); topArc.rotation.z = Math.PI * 0.35;
  const btmArc = new THREE.Mesh(new THREE.TorusGeometry(1.2, 0.28, 16, 32, Math.PI * 1.3), goldReliefMat);
  btmArc.position.set(0, -1.0, 0); btmArc.rotation.z = Math.PI * 1.35;
  const vBar = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 4.6, 24), goldReliefMat);
  dGroup.add(topArc); dGroup.add(btmArc); dGroup.add(vBar);
  return dGroup;
}

// Halos & Orbiting Crystal Shards
const ring1 = new THREE.Mesh(new THREE.TorusGeometry(6.2, 0.08, 16, 120), new THREE.MeshBasicMaterial({ color: 0x38BDF8, wireframe: true, transparent: true, opacity: 0.5 }));
ring1.rotation.x = Math.PI * 0.35;
```
