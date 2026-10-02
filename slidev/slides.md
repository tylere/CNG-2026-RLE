---
theme: default
title: Cloud-Native Geospatial for Country-Scale Ecosystem Risk Assessment
author: Tyler Erickson
colorSchema: dark
canvasWidth: 1600
aspectRatio: 16/9
transition: fade
background: ../images/hero_forest_coast.jpg
class: title-slide
---

# Cloud-Native Geospatial for Country-Scale Ecosystem Risk Assessment

CNG Forum 2026 · Cloud-Native Geo in Practice

Tyler Erickson

---
id: slide-speaker
layout: full-bleed
---

<div style="position:absolute; left:180px; top:230px" class="a-rise avatar">
  <img src="../images/speaker.png" width="420" alt="Tyler Erickson" />
</div>

<div style="position:absolute; left:720px; top:270px; width:800px">
  <span class="statement a-rise" style="--d:0.2s">Tyler Erickson</span><br>
  <span class="statement-sub a-rise" style="--d:0.4s"><span class="hl">VorGeo</span> · Founder</span><br>
  <span class="statement-sub a-rise" style="--d:0.6s"><span class="hl">Radiant Earth</span> · CTO</span>
  <div class="a-fade" style="--d:1s; margin-top:1.5rem">
    <a href="https://www.linkedin.com/in/tylere" class="mono">linkedin.com/in/tylere</a><br>
    <a href="https://github.com/tylere" class="mono">github.com/tylere</a><br>
    <a href="https://www.analyze.earth" class="mono">analyze.earth</a>
  </div>
</div>

---
id: slide-ecosystems
layout: full-bleed
---

<EcosystemScene />

---
id: slide-measure-ecosystems
layout: full-bleed
---

<MeasureEcosystemsSlide />

---
id: slide-camera-trap
layout: full-bleed
---

<CameraTrapSlide />

---
id: slide-wildlife-insights
layout: iframe
url: https://www.wildlifeinsights.org/
---

---
id: slide-question
layout: full-bleed
---

<div style="position:absolute; right:80px; top:40px" class="faint">
  <img src="../images/colombia_ecosystems.png" height="820" alt="Map of Colombia's ecosystems, each in a distinct color" />
</div>

<div style="position:absolute; left:100px; top:280px" class="left-v">
  <span class="statement a-rise">How at risk</span>
  <span class="statement a-rise" style="--d:0.3s">are a country's</span>
  <span class="statement hl a-rise" style="--d:0.6s">ecosystems?</span>
</div>

---
id: slide-rle
layout: full-bleed
---

<div style="position:absolute; top:50px; left:0; right:0; text-align:center">
  <span class="eyebrow">IUCN Red List of Ecosystems</span><br>
  <span class="statement-sub">The global standard for ecosystem risk</span>
</div>

<div style="position:absolute; left:120px; top:250px; --d:0.2s" class="a-rise shadow">
  <img src="../images/iucn_guidelines_cover.png" height="560" alt="Cover of the IUCN Red List of Ecosystems guidelines" />
</div>

<div v-click style="position:absolute; right:80px; top:250px">
  <div class="light-card">
    <img src="../images/get_hierarchy.png" width="900" alt="The six levels of the IUCN Global Ecosystem Typology" />
  </div>
</div>

---
id: slide-covers
layout: full-bleed
---

<div class="covers" style="height:100%; align-items:center">
  <div class="tilt-l a-rise" style="--d:0.1s">
    <img src="../images/colombia_2017_cover.jpg" alt="Cover of the 2017 Colombia Red List of Ecosystems report" />
  </div>
  <div class="tilt-r a-rise" style="--d:0.5s">
    <img src="../images/myanmar_2020_cover.jpg" alt="Cover of the 2020 Threatened ecosystems of Myanmar report" />
  </div>
</div>

---
id: slide-patchwork
layout: full-bleed
---

<div class="center-v" style="height:100%">
  <span class="statement a-rise">A patchwork of tools and ad hoc scripts</span>
  <span v-click class="statement-sub hl">hard to <strong>share</strong> · <strong>reproduce</strong> · <strong>maintain</strong></span>
</div>

---
id: slide-metrics
layout: full-bleed
---

<MetricsDiagram />

---
id: slide-colombia
layout: full-bleed
---

<div style="position:absolute; left:140px; top:40px" class="a-rise">
  <img src="../images/colombia_ecosystems.png" height="820" alt="Map of Colombia's ecosystems, each in a distinct color" />
</div>

<div style="position:absolute; left:900px; top:170px" class="stats">
  <div class="a-rise" style="--d:0.4s"><span class="num">460,350</span><span class="unit">ecosystem polygons</span></div>
  <div class="a-rise" style="--d:0.8s"><span class="num">87</span><span class="unit">ecosystem types</span></div>
  <div class="a-rise" style="--d:1.2s"><span class="num">1.7 GB</span><span class="unit">as GeoParquet</span></div>
</div>

<div style="position:absolute; left:900px; bottom:70px; width:660px" class="muted mono">
  IDEAM · 1:100,000 · 2024
</div>

---
id: slide-goal
layout: full-bleed
---

<div class="center-v" style="height:100%">
  <span class="statement a-rise">An open-source,</span>
  <span class="statement hl a-rise" style="--d:0.4s">cloud-native</span>
  <span class="statement a-rise" style="--d:0.8s">assessment workflow</span>
</div>

---
id: slide-no-server
layout: full-bleed
---

<svg class="canvas" viewBox="0 0 1600 900" aria-label="A server icon crossed out">
  <g transform="translate(660 170)" stroke="#F2F4F6" stroke-width="6" fill="none">
    <rect x="0" y="0" width="280" height="90" rx="12"/>
    <rect x="0" y="120" width="280" height="90" rx="12"/>
    <rect x="0" y="240" width="280" height="90" rx="12"/>
    <g fill="#F2F4F6" stroke="none">
      <circle cx="40" cy="45" r="10"/><circle cx="40" cy="165" r="10"/><circle cx="40" cy="285" r="10"/>
    </g>
    <path d="M90 45 H240 M90 165 H240 M90 285 H240" stroke-width="5"/>
  </g>
  <path class="draw" style="--d:0.5s" pathLength="1" d="M600 540 L1000 120" stroke="#e0595a" stroke-width="14" stroke-linecap="round" fill="none"/>
  <text x="800" y="680" text-anchor="middle" font-size="68" font-weight="700" class="a-rise" style="--d:1s">No geospatial server required</text>
</svg>

---
id: slide-architecture
layout: full-bleed
---

<ArchitectureDiagram />

---
id: slide-formats
layout: full-bleed
---

<FormatsDiagram />

---
id: slide-doc-as-code
layout: full-bleed
---

<div style="position:absolute; left:80px; top:200px; width:640px">
  <span class="eyebrow">Document as code</span>
  <span class="statement" style="display:block">This page is a notebook</span>
  <div v-click style="margin-top:1rem">
    <span class="statement-sub hl">code · narrative · maps</span>
    <div class="muted">one repo, version-controlled, reproducible</div>
  </div>
</div>

<div style="position:absolute; right:120px; top:40px; --d:0.3s" class="frame a-rise">
  <img src="../images/demo/criterion_b.png" height="780" alt="Rendered notebook output: convex hull of an ecosystem's distribution" />
</div>

---
id: slide-demo
layout: iframe
url: https://tylere.github.io/rle-tyler-colombia/
---

---
id: slide-backup-home
layout: full-bleed
---

<span class="eyebrow" style="position:absolute; top:20px; left:0">Backup</span>

<div class="center-v" style="height:100%">
  <div class="frame">
    <img src="../images/demo/home.png" height="720" alt="Home page of the Threatened ecosystems of Colombia assessment site" />
  </div>
</div>

---
id: slide-backup-assessment
layout: full-bleed
---

<span class="eyebrow" style="position:absolute; top:20px; left:0">Backup</span>

<div style="position:absolute; left:180px; top:110px" class="light-card">
  <img src="../images/demo/assessment.png" height="660" alt="Assessment table with Criterion B1 and B2 marked Least Concern" />
</div>

<div style="position:absolute; right:200px; top:60px" class="light-card">
  <img src="../images/demo/criterion_b.png" height="760" alt="Extent of occurrence convex hull for Agroecosistema Cafetero" />
</div>

---
id: slide-backup-map
layout: full-bleed
---

<span class="eyebrow" style="position:absolute; top:20px; left:0">Backup</span>

<div class="center-v" style="height:100%">
  <span class="muted">[Screenshot: interactive Lonboard map from the site]</span>
</div>

---
id: slide-hard-part
layout: full-bleed
---

<div class="center-v" style="height:100%">
  <span class="statement a-rise">The hard part wasn't the geospatial computation.</span>
  <span v-click class="statement hl" style="font-size:3.2em">It was setup.</span>
</div>

---
id: slide-friction
layout: full-bleed
---

<div style="position:absolute; top:50px; left:0; right:0; text-align:center">
  <span class="statement-sub">Assessors are ecologists, not software engineers</span>
</div>

<FrictionPile />

---
id: slide-setup
---

<span class="statement-sub">Setup friction as a first-class problem</span>

<SetupCards />

<a href="https://github.com/rle-assessment" style="position:absolute; bottom:60px; left:0">github.com/rle-assessment</a>

---
id: slide-falls-short
---

<span class="statement-sub">Where the tooling still falls short</span>

<ul class="lessons">
  <li v-click>Source data behind logins and manual downloads</li>
  <li v-click>Cloud auth and permissions are still the wall</li>
  <li v-click>Format details matter: GeoParquet row groups</li>
  <li v-click>CI builds that need retries</li>
</ul>

---
id: slide-takeaways
layout: full-bleed
---

<div class="center-v" style="height:100%; gap:2.2rem">
  <span class="statement-sub a-rise">Cloud-native formats make country-scale maps <strong>static</strong></span>
  <span v-click class="statement-sub">Document-as-code keeps the science <strong>reproducible</strong></span>
  <span v-click class="statement-sub hl">For non-engineers, <strong>setup is the product</strong></span>
</div>

---
id: slide-thanks
layout: full-bleed
background: ../images/hero_forest_coast.jpg
---

<div class="center-v deep-copy" style="height:100%">
  <span class="statement a-rise">Thank you</span>
  <a href="https://iucnrle.org/">iucnrle.org</a>
  <a href="https://github.com/rle-assessment">github.com/rle-assessment</a>
  <a href="https://tylere.github.io/rle-tyler-colombia/">tylere.github.io/rle-tyler-colombia</a>
</div>
