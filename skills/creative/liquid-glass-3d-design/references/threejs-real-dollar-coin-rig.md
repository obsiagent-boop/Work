# Three.js Authentic 3D Real Dollar Coin Rig

```javascript
function createRealDollarMesh() {
  const dGroup = new THREE.Group();
  
  const goldReliefMat = new THREE.MeshStandardMaterial({
    color: 0xFDE047,
    metalness: 0.98,
    roughness: 0.08
  });
  
  // High-Relief Double-Struck Serif Dollar Symbol ($)
  const topArc = new THREE.Mesh(new THREE.TorusGeometry(1.25, 0.3, 16, 36, Math.PI * 1.3), goldReliefMat);
  topArc.position.set(0, 1.05, 0); 
  topArc.rotation.z = Math.PI * 0.35;
  
  const btmArc = new THREE.Mesh(new THREE.TorusGeometry(1.25, 0.3, 16, 36, Math.PI * 1.3), goldReliefMat);
  btmArc.position.set(0, -1.05, 0); 
  btmArc.rotation.z = Math.PI * 1.35;
  
  // Double-Struck Vertical Spine Bars
  const bar1 = new THREE.Mesh(new THREE.CylinderGeometry(0.16, 0.16, 4.6, 24), goldReliefMat);
  bar1.position.set(-0.3, 0, 0);
  const bar2 = new THREE.Mesh(new THREE.CylinderGeometry(0.16, 0.16, 4.6, 24), goldReliefMat);
  bar2.position.set(0.3, 0, 0);
  
  dGroup.add(topArc); 
  dGroup.add(btmArc); 
  dGroup.add(bar1); 
  dGroup.add(bar2);
  return dGroup;
}

function buildFullCoin(coinGroup) {
  const goldCoreMat = new THREE.MeshStandardMaterial({
    color: 0xF59E0B,
    metalness: 0.95,
    roughness: 0.15,
    emissive: 0x92400E,
    emissiveIntensity: 0.2
  });
  
  const goldReliefMat = new THREE.MeshStandardMaterial({
    color: 0xFDE047,
    metalness: 0.98,
    roughness: 0.08
  });

  // Base Disc
  const coinGeo = new THREE.CylinderGeometry(4.2, 4.2, 0.5, 64);
  const coinMesh = new THREE.Mesh(coinGeo, goldCoreMat);
  coinMesh.rotation.x = Math.PI * 0.5;
  coinGroup.add(coinMesh);

  // Outer Beveled Rim
  const rimGeo = new THREE.TorusGeometry(4.2, 0.22, 16, 64);
  const rim = new THREE.Mesh(rimGeo, goldReliefMat);
  coinGroup.add(rim);

  // Front and Back Embossed Dollar
  const frontD = createRealDollarMesh();
  frontD.position.set(0, 0, 0.32);
  coinGroup.add(frontD);

  const backD = createRealDollarMesh();
  backD.position.set(0, 0, -0.32);
  backD.rotation.y = Math.PI;
  coinGroup.add(backD);

  // 48 Radial Reeding Teeth on Edge
  for (let i = 0; i < 48; i++) {
    const angle = (i / 48) * Math.PI * 2;
    const reed = new THREE.Mesh(new THREE.BoxGeometry(0.08, 0.52, 0.12), goldReliefMat);
    reed.position.set(Math.cos(angle) * 4.3, Math.sin(angle) * 4.3, 0);
    reed.rotation.z = angle;
    coinGroup.add(reed);
  }
}
```
