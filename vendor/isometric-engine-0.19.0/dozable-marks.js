// From src/doz-space/brand-marks.ts at 6957748 (engine 0.18.0): Dozable's mark "claude", for <isometric-diagram>.
import { registerMarks } from './isometric-diagram.js';

/** a burst of rays flat on the top face */
function claude(k, b) {
  const r = 0.78, cx = (b.x0 + b.x1) / 2, cy = (b.y0 + b.y1) / 2, z = b.z1 + 0.005, n = 12;
  let s = '';
  for (let i = 0; i < n; i++) {
    const a = i * 2 * Math.PI / n + 0.26, len = r * (i % 2 ? 0.78 : 1), r0 = r * 0.2;
    s += k.line3([cx + Math.cos(a) * r0, cy + Math.sin(a) * r0, z], [cx + Math.cos(a) * len, cy + Math.sin(a) * len, z], 'ico-claude');
  }
  return s;
}

registerMarks({
  icons: { claude },
  css: `
.ghost .ico-claude{opacity:.45}
.ico-claude{stroke:#d97757;stroke-width:3;stroke-linecap:round;fill:none}
`,
});
