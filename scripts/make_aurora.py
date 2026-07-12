import os

W, H = 860, 300
OUT = os.path.join(os.path.dirname(__file__), "..", "aurora.svg")

SVG = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <!-- Dark Background Gradient -->
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#09090b"/>
      <stop offset="100%" stop-color="#18181b"/>
    </linearGradient>

    <!-- Aurora Wave Gradient -->
    <linearGradient id="aurora" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#3b82f6"/> <!-- Blue -->
      <stop offset="35%" stop-color="#ec4899"/> <!-- Pink -->
      <stop offset="65%" stop-color="#d946ef"/> <!-- Magenta -->
      <stop offset="100%" stop-color="#60a5fa"/> <!-- Light Blue -->
    </linearGradient>

    <!-- Strong Blur for Aurora Effect -->
    <filter id="blur" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="40" result="blur"/>
    </filter>
    
    <!-- Subtle Text Shadow -->
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Base Background -->
  <rect width="{W}" height="{H}" fill="url(#bg)"/>

  <!-- The Aurora Waves -->
  <!-- We animate the path 'd' attribute to create an undulating liquid motion -->
  <g filter="url(#blur)">
    <!-- Main thick wave -->
    <path fill="none" stroke="url(#aurora)" stroke-width="90" stroke-linecap="round" opacity="0.8">
      <animate attributeName="d" 
        values="M-100,{H*0.7} Q{W*0.25},{H*0.2} {W*0.5},{H*0.6} T{W+100},{H*0.4};
                M-100,{H*0.4} Q{W*0.25},{H*0.8} {W*0.5},{H*0.3} T{W+100},{H*0.7};
                M-100,{H*0.7} Q{W*0.25},{H*0.2} {W*0.5},{H*0.6} T{W+100},{H*0.4}" 
        dur="12s" repeatCount="indefinite" />
    </path>
    
    <!-- Secondary overlapping wave for complexity -->
    <path fill="none" stroke="url(#aurora)" stroke-width="50" stroke-linecap="round" opacity="0.9">
      <animate attributeName="d" 
        values="M-100,{H*0.3} Q{W*0.3},{H*0.8} {W*0.6},{H*0.2} T{W+100},{H*0.7};
                M-100,{H*0.7} Q{W*0.3},{H*0.2} {W*0.6},{H*0.8} T{W+100},{H*0.3};
                M-100,{H*0.3} Q{W*0.3},{H*0.8} {W*0.6},{H*0.2} T{W+100},{H*0.7}" 
        dur="17s" repeatCount="indefinite" />
    </path>
  </g>

  <!-- Overlay Content -->
  <!-- Pill Badge (like "NEW Just shipped v2.0") -->
  <g transform="translate({W/2 - 110}, 65)">
    <rect width="220" height="28" rx="14" fill="#18181b" opacity="0.75" stroke="#3f3f46" stroke-width="1"/>
    <rect x="4" y="4" width="46" height="20" rx="10" fill="#ffffff"/>
    <text x="27" y="18" fill="#000000" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">NEW</text>
    <text x="130" y="18" fill="#e4e4e7" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif" font-size="12" text-anchor="middle">Generative AI Specialization</text>
  </g>

  <!-- Headline Text -->
  <g filter="url(#shadow)" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif" font-weight="800" text-anchor="middle">
    <text x="{W/2}" y="150" fill="#ffffff" font-size="42" letter-spacing="-0.5">
      Building AI systems that
    </text>
    <text x="{W/2}" y="205" fill="#ffffff" font-size="42" letter-spacing="-0.5">
      think, learn, and protect!
    </text>
  </g>
</svg>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(SVG)

print(f"wrote {OUT}")
