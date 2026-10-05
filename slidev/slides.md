---
theme: default
title: Cloud-Native Geospatial for Country-Scale Ecosystem Risk Assessment
author: Tyler Erickson
colorSchema: dark
canvasWidth: 1600
aspectRatio: 16/9
transition: fade
background: /images/hero_forest_coast.jpg
class: title-slide
---

# Cloud-Native Geospatial for Country-Scale Ecosystem Risk Assessment

CNG Forum 2026 · Cloud-Native Geo in Practice

Tyler Erickson

<!--
TODO
-->

---
id: slide-speaker
title: Tyler
layout: full-bleed
---

<div style="position:absolute; left:180px; top:230px" class="a-rise">
  <img src="/images/TylerErickson_400x400_bw.jpg" width="380" height="380" alt="Tyler Erickson" style="border-radius:50%; object-fit:cover; display:block; box-shadow:0 0 0 6px rgba(242,244,246,0.12)" />
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

<!--
TODO
-->

---
id: slide-ecosystems
title: Ecosystems
layout: full-bleed
---

<EcosystemScene>
  <text x="800" y="430" text-anchor="middle" font-size="120px" font-weight="700" fill="#F2F4F6" class="a-fade" style="--d:0.3s">Ecosystems</text>
</EcosystemScene>

<!--
"Ecosystems are complexes of organisms and their associated physical environment within a specified area (Tansley, 1935). They have four essential elements: a biotic complex, an abiotic environment, the interactions within and between them, and a physical space in which these operate (Pickett & Cadenasso, 1995)."
-->

---
id: slide-ecosystem-diagram
title: What Is an Ecosystem?
layout: full-bleed
---

<EcosystemDiagram />

<!--
Click 1: interactions within the biotic complex and within the abiotic environment.
Click 2: interactions between them.
Click 3: the physical space in which these operate.
-->

---
id: slide-measure-ecosystems
title: Measuring Ecosystems
layout: full-bleed
---

<MeasureEcosystemsSlide />

<!--
To assess ecosystem risk we need to measure what's happening on the ground. Field ecologists collect data: species counts, vegetation surveys, photographs, and physical samples — combined with satellite imagery and remote sensing to scale up to the country level.
-->

---
id: slide-camera-trap
title: Camera Traps
layout: full-bleed
---

<CameraTrapSlide />

<!--
Camera traps are triggered by motion and record wildlife continuously — including nocturnal behaviour invisible to daytime field surveys.
-->

---
id: slide-remote-sensing
title: Remote Sensing
layout: full-bleed
---

<RemoteSensingSlide />

<!--
TODO
-->

---
id: slide-iucn
title: IUCN
layout: full-bleed
---

<div style="position:absolute; left:120px; top:0; bottom:0; display:flex; align-items:center">
  <img src="/images/iucn_logo.svg" width="420" alt="IUCN logo" class="a-rise" style="background:white; border-radius:12px; padding:2rem" />
</div>

<div style="position:absolute; left:660px; top:0; bottom:0; display:flex; flex-direction:column; justify-content:center; gap:1.4rem">
  <span class="eyebrow a-rise">International Union for Conservation of Nature</span>
  <span class="statement a-rise" style="--d:0.2s; font-size:4em">IUCN</span>
  <span class="statement-sub a-rise" style="--d:0.4s">Independent · founded <span class="hl">1948</span></span>
  <span class="statement-sub a-rise" style="--d:0.6s">UN General Assembly <span class="hl">observer</span></span>
  <span v-click class="statement-sub">Drafted the <span class="hl">Convention on<br>Biological Diversity</span></span>
</div>

<a href="https://iucn.org/about-iucn" style="position:absolute; bottom:52px; right:80px" class="mono muted">iucn.org/about-iucn</a>

<!--
TODO
-->

---
id: slide-cbd
title: Convention on Biological Diversity
layout: full-bleed
---

<div class="center-v a-rise" style="height:100%">
  <a href="https://www.cbd.int/" target="_blank" class="frame">
    <img src="/images/cbd_home.png" style="height:720px; width:auto; display:block" alt="Home page of the Convention on Biological Diversity website, cbd.int" />
  </a>
</div>

<a href="https://www.cbd.int/" target="_blank" style="position:absolute; bottom:52px; right:80px" class="mono muted">cbd.int</a>

<!--
Meeting later the month for its first global review of progress in implementing the Kumming-Montreal Global Biodiversity Framework.
-->

---
id: slide-iucnrle-site
title: Red List of Ecosystems Site
layout: iframe
url: https://iucnrle.org/
---

<!--
TODO
-->

---
id: slide-guidelines
title: RLE Guidelines
layout: full-bleed
---

<div style="position:absolute; left:160px; top:0; bottom:0; display:flex; flex-direction:column; justify-content:center" class="a-rise">
  <span class="book face-right" style="--pages:177"><img src="/images/iucn_rle_guidelines_2024_cover.jpg" style="height:620px; width:auto" alt="Cover of the Guidelines for the application of IUCN Red List of Ecosystems Categories and Criteria, version 2.0" class="shadow" /></span>
  <div class="statement-sub" style="text-align:center; margin-top:1.5rem"><span class="hl">177</span> pages</div>
</div>

<div style="position:absolute; left:820px; width:680px; top:0; bottom:0; display:flex; flex-direction:column; justify-content:center; gap:1.4rem">
  <span class="eyebrow a-rise">IUCN Red List of Ecosystems</span>
  <span class="statement a-rise" style="--d:0.2s">Ecosystem Assessment Guidelines</span>
  <span class="statement-sub a-rise" style="--d:0.4s">· <span class="hl">2024</span></span></div>

<!--
TODO
-->

---
id: slide-global-ecosystems
title: Global Ecosystems Explorer
layout: iframe
url: https://global-ecosystems.org/explore
---

<!--
- Dismiss the dialogs
- Go to the Analyze tab
- Zoom map to Little Cottonwood Canyon
- Query the ecosystems
-->

---
id: slide-covers
title: Country Assessments
layout: full-bleed
---

<div class="covers" style="height:100%; align-items:center">
  <div class="tilt-l a-rise" style="--d:0.1s">
    <a href="https://www.conservation.org.co/media/A7.LRE-Colombia_INFORME%20FINAL_%202017.pdf" target="_blank" class="book" style="--pages:142"><img src="/images/colombia_2017_cover.jpg" alt="Cover of the 2017 Colombia Red List of Ecosystems report" /></a>
    <div class="statement-sub" style="text-align:center; margin-top:1.5rem"><span class="hl">142</span> pages</div>
  </div>
  <div class="tilt-r a-rise" style="--d:0.5s">
    <a href="https://library.wcs.org/DesktopModules/Bring2mind/DMX/API/Entries/Download?EntryId=37457&PortalId=0&DownloadMethod=attachment" target="_blank" class="book" style="--pages:395"><img src="/images/myanmar_2020_cover.jpg" alt="Cover of the 2020 Threatened ecosystems of Myanmar report" /></a>
    <div class="statement-sub" style="text-align:center; margin-top:1.5rem"><span class="hl">395</span> pages</div>
  </div>
</div>

<!--
Long reports, not for the faint hearted.

-->

---
id: slide-easier
title: Make It Easier
layout: full-bleed
---

<div class="center-v" style="height:100%">
  <span class="statement a-rise">How do we make it <span class="hl">easier</span></span>
  <span class="statement a-rise" style="--d:0.3s">to perform an ecosystem assessment?</span>
</div>

<!--
TODO
-->

---
id: slide-guidelines-rle-python
title: Guidelines to rle-python
layout: full-bleed
---

<!-- Top half: guidelines → rle-python -->
<div style="position:absolute; left:192px; top:45px" class="a-rise">
  <span class="book face-right" style="--pages:177"><img src="/images/iucn_rle_guidelines_2024_cover.jpg" style="height:360px; width:auto" alt="Cover of the Guidelines for the application of IUCN Red List of Ecosystems Categories and Criteria, version 2.0" class="shadow" /></span>
</div>

<!-- Bottom half: Global Ecosystem Typology explorer → iucn-get-data -->
<div style="position:absolute; left:60px; top:505px" class="a-rise" >
  <span class="book face-right screen" style="--pages:220"><img src="/images/global_ecosystems_explore.jpg" style="width:540px; height:auto" alt="Explore page of the Global Ecosystem Typology website, global-ecosystems.org" class="shadow" /></span>
</div>

<div style="position:absolute; left:660px; top:100px" class="a-rise">
  <span class="repo-label">GitHub repositories</span>
</div>
<div class="repo-group a-rise" style="position:absolute; left:660px; top:140px; width:400px; height:620px"></div>
<div class="repo-node a-rise" style="position:absolute; left:680px; top:183px">rle-python</div>
<div class="repo-node a-rise" style="position:absolute; left:680px; top:633px">iucn-get-data</div>

<svg class="canvas" viewBox="0 0 1600 900" style="position:absolute; inset:0; pointer-events:none">
  <path class="edge draw" style="--d:0.6s" pathLength="1" d="M447 320 C 560 320, 540 232, 666 232"/>
  <polygon class="a-fade" style="--d:1.2s" points="682,232 662,221 662,243" fill="#FFD626"/>
  <path class="edge draw" style="--d:0.8s" pathLength="1" d="M570 770 C 610 770, 600 682, 666 682"/>
  <polygon class="a-fade" style="--d:1.4s" points="682,682 662,671 662,693" fill="#FFD626"/>

  <!-- Data + calculations (as on slide 16) -->
  <g v-click>
    <rect class="node" x="1110" y="60" width="420" height="190" rx="14"/>
    <image href="/images/colombia_ecosystems.png" x="1384" y="72" width="122" height="166"/>
    <text x="1140" y="140" font-size="34px" font-weight="700">Ecosystem</text>
    <text x="1140" y="184" font-size="34px" font-weight="700">map data</text>
    <path class="edge" d="M1320 250 L1320 366"/>
    <polygon points="1320,382 1309,362 1331,362" fill="#FFD626"/>
    <path class="edge" d="M1040 232 C 1080 232, 1070 440, 1094 440"/>
    <polygon points="1110,440 1090,429 1090,451" fill="#FFD626"/>
    <path class="edge" d="M1040 682 C 1080 682, 1070 475, 1094 475"/>
    <polygon points="1110,475 1090,464 1090,486" fill="#FFD626"/>
    <rect class="node key" x="1110" y="382" width="420" height="150" rx="14"/>
    <text x="1320" y="449" text-anchor="middle" font-size="34px" font-weight="700">RLE criteria</text>
    <text x="1320" y="493" text-anchor="middle" font-size="34px" font-weight="700">calculations</text>
  </g>
</svg>

<style>
.repo-label {
  font-family: 'Berkeley Mono', monospace;
  font-size: 22px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: rgba(242, 244, 246, 0.55);
}
.repo-group {
  box-sizing: border-box;
  border: 2px dashed rgba(242, 244, 246, 0.25);
  border-radius: 16px;
}
.repo-node {
  width: 360px;
  padding: 22px 0;
  text-align: center;
  font-family: 'Berkeley Mono', monospace;
  font-size: 32px;
  background: rgba(65, 139, 217, 0.12);
  border: 3px solid #418BD9;
  border-radius: 14px;
  box-sizing: border-box;
}
</style>

<!--
TODO
-->

---
id: slide-architecture
title: Architecture
layout: full-bleed
---

<ArchitectureDiagram />

<!--
TODO
-->

---
id: slide-colombia-site
title: Colombia Assessment Site
layout: iframe
url: https://tylere.github.io/rle-tyler-colombia/
---

<!--
TODO
-->

---
id: slide-wildlife-insights
title: Wildlife Insights
layout: full-bleed
---

<div style="position:absolute; inset:0; overflow:hidden">
  <img src="/images/demo/home.png" style="width:100%; height:100%; object-fit:cover; object-position:top" alt="Wildlife Insights dashboard" />
</div>

<!--
Wildlife Insights is an AI-powered platform that helps researchers process and share camera trap data at scale — using machine learning to identify species in images, reducing the manual work from months to hours.
-->

---
id: slide-gbf-indicator
title: GBF Indicator A.2
layout: full-bleed
---

<!-- Paper, centered at full height -->
<div style="position:absolute; inset:20px 0; display:flex; justify-content:center" class="a-rise">
  <a href="https://doi.org/10.32942/X25955" target="_blank">
    <img src="/images/buschke_extent_natural_ecosystems.png" style="height:860px; width:auto; display:block" alt="First page of Buschke et al., Reporting on the extent of natural ecosystems under the Kunming-Montreal Global Biodiversity Framework" class="shadow" />
  </a>
</div>

<!-- Figure 1, overlapping the paper -->
<div style="left:448px; top:196px" class="fig-card" v-click="1">
  <img src="/images/buschke_fig1_reporting_status.png" style="width:680px; height:auto; display:block" alt="Figure 1 from Buschke et al.: reporting status for Indicator A.2 across the 196 Parties to the CBD — 31.1% did not submit a 7th National Report, 29.1% did not report A.2, 9.2% incomplete, 30.6% complete" />
</div>

<!-- Figure 2, overlapping Figure 1's caption -->
<div style="left:448px; top:490px" class="fig-card" v-click="2">
  <img src="/images/buschke_fig2_sources_disaggregation.png" style="width:680px; height:auto; display:block" alt="Figure 2 from Buschke et al.: (a) data sources and (b) type of disaggregation used by the 78 Parties that reported Indicator A.2 — land cover and ecosystem maps are the most common sources; most Parties reported no disaggregation" />
  <!-- Highlights (positions are the figure's pixels × 680/1456, plus the 12px card padding) -->
  <div class="fig-hl" style="left:40px; top:74px; width:229px; height:30px"></div>
  <div class="fig-hl" style="left:425px; top:86px; width:150px; height:23px"></div>
</div>

<style>
/* Figures 1 and 2 share one scale (680px wide ≈ 0.467 × their ~1455px originals) so their text matches */
.fig-card {
  position: absolute;
  background: #fff;
  padding: 12px;
  border: 4px solid #418BD9;
  border-radius: 10px;
  box-shadow: 0 0 36px rgba(0, 0, 0, 0.6);
}
/* Highlights fade in shortly after Figure 2 is revealed (no extra click) */
.fig-hl {
  opacity: 0;
  position: absolute;
  border: 3px solid #FFD626;
  border-radius: 6px;
  background: rgba(255, 214, 38, 0.18);
  box-shadow: 0 0 12px rgba(255, 214, 38, 0.6);
}
.fig-card:not(.slidev-vclick-hidden) .fig-hl {
  animation: fade-in 0.6s ease-out 0.8s both;
}
</style>

<!--
Source of images: Buschke et al., "Reporting on the extent of natural ecosystems under the Kunming-Montreal Global Biodiversity Framework" — https://doi.org/10.32942/X25955
-->

---
id: slide-ideam
title: IDEAM Ecosystems
layout: full-bleed
---

<div style="position:absolute; left:100px; width:560px; top:0; bottom:0; display:flex; flex-direction:column; justify-content:center; gap:1.4rem">
  <span class="eyebrow a-rise">Country ecosystem map example</span>
  <span class="statement a-rise" style="--d:0.2s; font-size:4em">Colombia Ecosystems</span>
  <ul class="lessons a-rise" style="--d:0.4s; list-style:none; padding:0; margin:0">
    <li>SharePoint site (required manual download)</li>
    <li>2.1 GB file size</li>
    <li>1 minute to download (high-speed connection)</li>
    <li>ESRI Shapefile and Geodatabase format</li>
  </ul>
  <a href="https://www.ideam.gov.co/ecosistemas" target="_blank" class="mono muted a-fade" style="--d:0.6s">ideam.gov.co/ecosistemas</a>
</div>

<div style="position:absolute; right:80px; top:0; bottom:0; display:flex; align-items:center" class="a-rise">
  <a href="https://www.ideam.gov.co/ecosistemas" target="_blank" class="frame">
    <img src="/images/ideam_ecosistemas.png" style="height:800px; width:auto; display:block" alt="IDEAM Ecosistemas page, with a card to download the 2024 1:100,000 ecosystem map of Colombia" />
  </a>
</div>

<!-- Highlight the download card (grid lower-left): page pixels × 800/1192, offset by the frame's position -->
<div class="a-fade" style="--d:1s; position:absolute; left:748px; top:731px; width:209px; height:133px; border:3px solid #FFD626; border-radius:6px; background:rgba(255,214,38,0.15); box-shadow:0 0 14px rgba(255,214,38,0.6); pointer-events:none"></div>

<!--
TODO
-->

---
id: slide-source-coop
title: Source Cooperative
layout: iframe
url: https://source.coop/tyler/colombia-ecosystems-map
---

<!--
TODO
-->

---
id: slide-colombia
title: Colombia
layout: full-bleed
---

<div style="position:absolute; left:140px; top:40px" class="a-rise">
  <img src="/images/colombia_ecosystems.png" height="820" alt="Map of Colombia's ecosystems, each in a distinct color" />
</div>

<div style="position:absolute; left:700px; width:860px; top:130px" class="stats">
  <div class="a-rise" style="--d:0.4s"><span class="num">460,350</span><span class="unit">ecosystem polygons</span></div>
  <div class="a-rise" style="--d:0.8s"><span class="num">87</span><span class="unit">ecosystem types</span></div>
  <div class="a-rise" style="--d:1.2s"><span class="num">1.7 GB</span><span class="unit">as GeoParquet</span></div>
  <div class="a-rise unit" style="--d:1.6s; display:block; margin:1.2rem 0 0">Also rasterized to 10m...</div>
  <div class="a-rise" style="--d:2s"><span class="num">520 MB</span><span class="unit">as Cloud-optimized GeoTIFF</span></div>
</div>

<!--
TODO
-->

---
id: slide-cloud-optimized
title: Cloud-Optimized Formats
layout: full-bleed
---

<div class="center-v" style="height:100%; gap:2.4rem">
  <span class="statement a-rise" style="max-width:1300px; text-align:center"><span class="hl">Cloud-optimized</span> data formats are what make this workflow sing!</span>
  <span class="statement-sub a-rise" style="--d:0.6s; max-width:1100px; text-align:center">Reproducible, highly-interactive reports based on static files instead of squinting at static PDFs.</span>
</div>

<!--
TODO
-->

---
id: slide-question
title: How At Risk?
layout: full-bleed
---

<div style="position:absolute; right:80px; top:40px; opacity:0.85">
  <img src="/images/colombia_ecosystems.png" height="820" alt="Map of Colombia's ecosystems, each in a distinct color" />
</div>

<div style="position:absolute; left:100px; top:220px" class="left-v">
  <span class="statement a-rise" style="font-size:4em">How at risk</span>
  <span class="statement a-rise" style="--d:0.3s; font-size:4em">are a country's</span>
  <span class="statement hl a-rise" style="--d:0.6s; font-size:4em">ecosystems?</span>
</div>

<!--
TODO
-->

---
id: slide-rle
title: Red List of Ecosystems
layout: full-bleed
---

<div style="position:absolute; top:50px; left:0; right:0; text-align:center">
  <span class="eyebrow">IUCN Red List of Ecosystems</span><br>
  <span class="statement-sub">The global standard for ecosystem risk</span>
</div>

<div style="position:absolute; left:120px; top:250px; --d:0.2s" class="a-rise shadow">
  <img src="/images/iucn_guidelines_cover.png" height="560" alt="Cover of the IUCN Red List of Ecosystems guidelines" />
</div>

<div v-click style="position:absolute; right:80px; top:250px">
  <div class="light-card">
    <img src="/images/get_hierarchy.png" width="900" alt="The six levels of the IUCN Global Ecosystem Typology" />
  </div>
</div>

<!--
The ecological counterpart to the Red List of Threatened Species. Global Ecosystem Typology gives the shared classification.
-->

---
id: slide-patchwork
title: Patchwork of Tools
layout: full-bleed
---

<div class="center-v" style="height:100%">
  <span class="statement a-rise">A patchwork of tools and ad hoc scripts</span>
  <span v-click class="statement-sub hl">hard to <strong>share</strong> · <strong>reproduce</strong> · <strong>maintain</strong></span>
</div>

<!--
TODO
-->

---
id: slide-metrics
title: Metrics
layout: full-bleed
---

<MetricsDiagram />

<!--
Integrate national-scale spatial data, compute metrics, produce a formal report meeting IUCN criteria.
-->

---
id: slide-goal
title: Goal
layout: full-bleed
---

<div class="center-v" style="height:100%">
  <span class="statement a-rise">An open-source,</span>
  <span class="statement hl a-rise" style="--d:0.4s">cloud-native</span>
  <span class="statement a-rise" style="--d:0.8s">assessment workflow</span>
</div>

<!--
TODO
-->

---
id: slide-no-server
title: No Server Required
layout: full-bleed
---

<svg class="canvas" viewBox="0 0 1600 900" style="width:100%;height:100%" aria-label="A server icon crossed out">
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
  <text x="800" y="680" text-anchor="middle" font-size="68px" font-weight="700" class="a-rise" style="--d:1s">No geospatial server required</text>
</svg>

<!--
TODO
-->

---
id: slide-formats
title: Formats
layout: full-bleed
---

<FormatsDiagram />

<!--
TODO
-->

---
id: slide-doc-as-code
title: Document as Code
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
  <img src="/images/demo/criterion_b.png" height="780" alt="Rendered notebook output: convex hull of an ecosystem's distribution" />
</div>

<!--
TODO
-->

---
id: slide-demo
title: Demo
layout: iframe
url: https://tylere.github.io/rle-tyler-colombia/
---

<!--
Live site: https://tylere.github.io/rle-tyler-colombia/
If the network fails, the next slides are screenshots.
-->

---
id: slide-backup-home
title: "Backup: Home"
layout: full-bleed
---

<span class="eyebrow" style="position:absolute; top:20px; left:0">Backup</span>

<div class="center-v" style="height:100%">
  <div class="frame">
    <img src="/images/demo/home.png" height="720" alt="Home page of the Threatened ecosystems of Colombia assessment site" />
  </div>
</div>

<!--
TODO
-->

---
id: slide-backup-assessment
title: "Backup: Assessment"
layout: full-bleed
---

<span class="eyebrow" style="position:absolute; top:20px; left:0">Backup</span>

<div style="position:absolute; left:180px; top:110px" class="light-card">
  <img src="/images/demo/assessment.png" height="660" alt="Assessment table with Criterion B1 and B2 marked Least Concern" />
</div>

<div style="position:absolute; right:200px; top:60px" class="light-card">
  <img src="/images/demo/criterion_b.png" height="760" alt="Extent of occurrence convex hull for Agroecosistema Cafetero" />
</div>

<!--
TODO
-->

---
id: slide-backup-map
title: "Backup: Map"
layout: full-bleed
---

<span class="eyebrow" style="position:absolute; top:20px; left:0">Backup</span>

<div class="center-v" style="height:100%">
  <span class="muted">[Screenshot: interactive Lonboard map from the site]</span>
</div>

<!--
TODO
-->

---
id: slide-hard-part
title: The Hard Part
layout: full-bleed
---

<div class="center-v" style="height:100%">
  <span class="statement a-rise">The hard part wasn't the geospatial computation.</span>
  <span v-click class="statement hl" style="font-size:3.2em">It was setup.</span>
</div>

<!--
TODO
-->

---
id: slide-friction
title: Friction
layout: full-bleed
---

<div style="position:absolute; top:50px; left:0; right:0; text-align:center">
  <span class="statement-sub">Assessors are ecologists, not software engineers</span>
</div>

<FrictionPile />

<!--
TODO
-->

---
id: slide-setup
title: Setup
layout: full-bleed
---

<div style="position:absolute; left:100px; right:100px; top:80px">
  <span class="statement-sub">Setup friction as a first-class problem</span>
  <SetupCards />
</div>

<a href="https://github.com/rle-assessment" style="position:absolute; bottom:52px; left:100px">github.com/rle-assessment</a>

<!--
TODO
-->

---
id: slide-falls-short
title: Where Tooling Falls Short
---

<span class="statement-sub">Where the tooling still falls short</span>

<ul class="lessons">
  <li v-click>Source data behind logins and manual downloads</li>
  <li v-click>Cloud auth and permissions are still the wall</li>
  <li v-click>Format details matter: GeoParquet row groups</li>
  <li v-click>CI builds that need retries</li>
</ul>

<!--
TODO
-->

---
id: slide-takeaways
title: Takeaways
layout: full-bleed
---

<div class="center-v" style="height:100%; gap:2.2rem">
  <span class="statement-sub a-rise">Cloud-native formats make country-scale maps <strong>static</strong></span>
  <span v-click class="statement-sub">Document-as-code keeps the science <strong>reproducible</strong></span>
  <span v-click class="statement-sub hl">For non-engineers, <strong>setup is the product</strong></span>
</div>

<!--
TODO
-->

---
id: slide-thanks
title: Thank You
layout: full-bleed
background: /images/hero_forest_coast.jpg
---

<div class="center-v deep-copy" style="height:100%">
  <span class="statement a-rise">Thank you</span>
  <a href="https://iucnrle.org/">iucnrle.org</a>
  <a href="https://github.com/rle-assessment">github.com/rle-assessment</a>
  <a href="https://tylere.github.io/rle-tyler-colombia/">tylere.github.io/rle-tyler-colombia</a>
</div>

<!--
TODO
-->
