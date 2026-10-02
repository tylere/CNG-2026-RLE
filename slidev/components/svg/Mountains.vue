<template>
  <g class="mountains">
    <defs>
      <linearGradient id="side-ground" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="#26412d"/><stop offset="1" stop-color="#3e6d3b"/>
      </linearGradient>
      <radialGradient id="side-sun">
        <stop offset="0.45" stop-color="#FFD626" stop-opacity="0.45"/><stop offset="1" stop-color="#FFD626" stop-opacity="0"/>
      </radialGradient>
      <radialGradient id="side-water" cx="0.45" cy="0.4" r="0.6">
        <stop offset="0" stop-color="#3b84b5"/><stop offset="1" stop-color="#1f557c"/>
      </radialGradient>
    </defs>
    <defs>
      <radialGradient id="side-glow">
        <stop offset="0" stop-color="#ff9a4a" stop-opacity="0.55"/><stop offset="1" stop-color="#ff9a4a" stop-opacity="0"/>
      </radialGradient>
    </defs>
    <polygon points="-320.0,470.0 -180.0,410.0 -60.0,470.0 90.0,395.0 230.0,455.0 370.0,380.0 520.0,445.0 690.0,410.0 850.0,470.0 1010.0,385.0 1160.0,440.0 1300.0,375.0 1450.0,430.0 1600.0,400.0 1740.0,455.0 1920.0,405.0 1920.0,600.0 -320.0,600.0" fill="#404a55"/>
    <polygon points="-180.0,410.0 -146.4,426.8 -174.0,432.0 -188.0,426.0 -219.2,426.8" fill="#8b9197"/>
    <polygon points="90.0,395.0 129.2,411.8 96.0,417.0 82.0,411.0 48.0,416.0" fill="#8b9197"/>
    <polygon points="370.0,380.0 412.0,398.2 376.0,402.0 362.0,396.0 330.8,401.0" fill="#8b9197"/>
    <polygon points="690.0,410.0 734.8,426.8 696.0,432.0 682.0,426.0 642.4,419.8" fill="#8b9197"/>
    <polygon points="1010.0,385.0 1052.0,400.4 1016.0,407.0 1002.0,401.0 965.2,408.8" fill="#8b9197"/>
    <polygon points="1300.0,375.0 1342.0,390.4 1306.0,397.0 1292.0,391.0 1260.8,393.2" fill="#8b9197"/>
    <polygon points="1600.0,400.0 1639.2,415.4 1606.0,422.0 1592.0,416.0 1558.0,408.4" fill="#8b9197"/>
    <path d="M-320 600 L-320 530 Q-150 480 -20 540 Q120 470 300 525 Q470 575 640 520 Q820 465 1000 530 Q1180 585 1350 515 Q1500 470 1620 520 Q1760 565 1920 505 L1920 600 Z" fill="#284031"/>
    <rect x="-320" y="585" width="2240" height="515" fill="url(#side-ground)"/>
  </g>
</template>
