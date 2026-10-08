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

<div style="position:absolute; inset:0; display:flex; align-items:center; justify-content:center; gap:120px">
<div class="a-rise">
  <img src="/images/TylerErickson_400x400_bw.jpg" alt="Tyler Erickson" style="width:380px; height:380px; border-radius:50%; object-fit:cover; display:block; box-shadow:0 0 0 6px rgba(242,244,246,0.12)" />
</div>

<div>
  <span class="statement a-rise" style="--d:0.2s">Tyler Erickson</span><br>
  <span class="statement-sub a-rise" style="--d:0.4s"><span class="hl">VorGeo</span> · Founder</span><br>
  <span class="statement-sub a-rise" style="--d:0.6s"><span class="hl">Radiant Earth</span> · CTO</span>
  <div class="a-fade" style="--d:1s; margin-top:1.5rem">
    <a href="https://www.linkedin.com/in/tylere" class="mono">linkedin.com/in/tylere</a><br>
    <a href="https://github.com/tylere" class="mono">github.com/tylere</a><br>
    <a href="https://www.analyze.earth" class="mono">analyze.earth</a>
  </div>
</div>
</div>

<div class="muted a-fade" style="--d:1.2s; position:absolute; left:0; right:0; bottom:52px; text-align:center; font-size:1.6rem">
  The work described in this presentation was funded by Google
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
- I am not an ecologist, by training.
"Ecosystems are complexes of organisms and their associated physical environment within a specified area (Tansley, 1935). 
- They have four essential elements: a biotic complex, an abiotic environment, the interactions within and between them, and a physical space in which these operate (Pickett & Cadenasso, 1995)."
-->

---
id: slide-ecosystem-diagram
title: What Is an Ecosystem?
layout: full-bleed
---

<EcosystemDiagram />

<!--
- composed of two main systems
- [**C1**] Systems interact internally
  - animals eat plants. animals eat other animals. some plants eat animals.
  - water erodes rock and makes soil
- **[C2]** Abiotic environment affects the biotic complex
  - plants & animals need water & light
  - fire, floods, drought are threats
- **[C3]** Biotic -> Abiotic
  - Anthropomorphic change
  - Beavers affect water & land
  - Coral, mangroves affects oceans
-->

---
id: slide-measure-ecosystems
title: Measuring Ecosystems
layout: full-bleed
---

<MeasureEcosystemsSlide />

<!--
Field measurements
- species counts, vegetation surveys, photographs, and physical samples
-->

---
id: slide-camera-trap
title: Automated sensors
layout: full-bleed
clicks: 1
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
What other sensors?
- aircraft
- drones
- satellites
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
  <span class="statement-sub a-rise" style="--d:0.4s">Independent Organization</span>
  <span class="statement-sub a-rise" style="--d:0.6s">Founded <span class="hl">1948</span></span>
  <span class="statement-sub a-rise" style="--d:0.8s">UN General Assembly <span class="hl">observer</span></span>
</div>

<blockquote class="a-fade" style="--d:1.2s; position:absolute; left:120px; right:120px; bottom:120px; margin:0; padding-left:1.2rem; border-left:4px solid #FFD626; font-size:1.6rem; font-style:italic; color:rgba(242,244,246,0.85)">
  “[IUCN is] the global authority on the status of the natural world and the measures needed to safeguard it.”
</blockquote>

<a href="https://iucn.org/about-iucn" style="position:absolute; bottom:52px; right:80px" class="mono muted">iucn.org/about-iucn</a>

<!--
Who cares about conservation?
At the international level...
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
id: slide-acronyms
title: International Acronyms
layout: full-bleed
---

<svg class="canvas" viewBox="0 0 1600 900" style="width:100%;height:100%" aria-label="How IUCN, CBD, COP, KMGBF, NBSAPs, National Reports, COP17 and the RLE relate">
  <defs>
    <marker id="acronym-arrow" viewBox="0 0 10 10" refX="2" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M0 0 L10 5 L0 10 Z" fill="#FFD626"/>
    </marker>
  </defs>
  <text class="label" x="800" y="95" text-anchor="middle">WHO'S WHO IN INTERNATIONAL BIODIVERSITY POLICY</text>
    <g>
      <rect class="node" x="110" y="150" width="360" height="200" rx="14"/>
      <text x="290" y="218" text-anchor="middle" font-size="52px" font-weight="700">IUCN</text>
      <text x="290" y="262" text-anchor="middle" font-size="28px" style="fill:#FFD626">Science &amp; standards</text>
      <text x="290" y="308" text-anchor="middle" font-size="20px" opacity="0.6">International Union for</text>
      <text x="290" y="334" text-anchor="middle" font-size="20px" opacity="0.6">Conservation of Nature</text>
    </g>
    <g v-click>
      <rect class="node" x="620" y="150" width="360" height="200" rx="14"/>
      <text x="800" y="218" text-anchor="middle" font-size="52px" font-weight="700">CBD</text>
      <text x="800" y="262" text-anchor="middle" font-size="28px" style="fill:#FFD626">The treaty (1992)</text>
      <text x="800" y="308" text-anchor="middle" font-size="20px" opacity="0.6">Convention on</text>
      <text x="800" y="334" text-anchor="middle" font-size="20px" opacity="0.6">Biological Diversity</text>
      <path class="edge" d="M470 250 L612 250" marker-end="url(#acronym-arrow)"/>
      <text x="545" y="232" text-anchor="middle" font-size="19px" opacity="0.75" font-family="Berkeley Mono, monospace">drafted</text>
    </g>
    <g v-click>
      <rect class="node" x="1130" y="150" width="360" height="200" rx="14"/>
      <text x="1310" y="218" text-anchor="middle" font-size="52px" font-weight="700">COP</text>
      <text x="1310" y="262" text-anchor="middle" font-size="28px" style="fill:#FFD626">Governing body</text>
      <text x="1310" y="308" text-anchor="middle" font-size="20px" opacity="0.6">Conference of the Parties</text>
      <path class="edge" d="M980 250 L1122 250" marker-end="url(#acronym-arrow)"/>
      <text x="1055" y="232" text-anchor="middle" font-size="19px" opacity="0.75" font-family="Berkeley Mono, monospace">governed by</text>
    </g>
    <g v-click>
      <rect class="node" x="1225" y="560" width="260" height="200" rx="14"/>
      <text x="1355" y="628" text-anchor="middle" font-size="52px" font-weight="700">KMGBF</text>
      <text x="1355" y="670" text-anchor="middle" font-size="23px" style="fill:#FFD626">The plan (2022)</text>
      <text x="1355" y="702" text-anchor="middle" font-size="17px" opacity="0.6">Kunming-Montreal Global</text>
      <text x="1355" y="724" text-anchor="middle" font-size="17px" opacity="0.6">Biodiversity Framework</text>
      <path class="edge" d="M1310 350 L1310 552" marker-end="url(#acronym-arrow)"/>
      <text x="1325" y="460" text-anchor="start" font-size="19px" opacity="0.75" font-family="Berkeley Mono, monospace">adopted</text>
    </g>
    <g v-click>
      <rect class="node" x="855" y="560" width="260" height="200" rx="14"/>
      <text x="985" y="628" text-anchor="middle" font-size="52px" font-weight="700">NBSAPs</text>
      <text x="985" y="670" text-anchor="middle" font-size="23px" style="fill:#FFD626">Action plans</text>
      <text x="985" y="702" text-anchor="middle" font-size="17px" opacity="0.6">National Biodiversity</text>
      <text x="985" y="724" text-anchor="middle" font-size="17px" opacity="0.6">Strategies and</text>
      <text x="985" y="746" text-anchor="middle" font-size="17px" opacity="0.6">Action Plans</text>
      <path class="edge" d="M1225 660 L1123 660" marker-end="url(#acronym-arrow)"/>
      <text x="1170" y="625" text-anchor="middle" font-size="14px" opacity="0.75" font-family="Berkeley Mono, monospace">implemented</text>
      <text x="1170" y="646" text-anchor="middle" font-size="14px" opacity="0.75" font-family="Berkeley Mono, monospace">via</text>
    </g>
    <g v-click>
      <rect class="node" x="485" y="560" width="260" height="200" rx="14"/>
      <text x="615" y="608" text-anchor="middle" font-size="34px" font-weight="700">National</text>
      <text x="615" y="648" text-anchor="middle" font-size="34px" font-weight="700">Reports</text>
      <text x="615" y="690" text-anchor="middle" font-size="23px" style="fill:#FFD626">Progress</text>
      <text x="615" y="722" text-anchor="middle" font-size="17px" opacity="0.6">e.g. 7th National</text>
      <text x="615" y="744" text-anchor="middle" font-size="17px" opacity="0.6">Reports (Feb 2026)</text>
      <path class="edge" d="M855 660 L753 660" marker-end="url(#acronym-arrow)"/>
      <text x="800" y="625" text-anchor="middle" font-size="16px" opacity="0.75" font-family="Berkeley Mono, monospace">progress</text>
      <text x="800" y="646" text-anchor="middle" font-size="16px" opacity="0.75" font-family="Berkeley Mono, monospace">reported in</text>
    </g>
    <g v-click>
      <rect class="node" x="115" y="560" width="260" height="200" rx="14"/>
      <text x="245" y="628" text-anchor="middle" font-size="52px" font-weight="700">COP17</text>
      <text x="245" y="670" text-anchor="middle" font-size="23px" style="fill:#FFD626">Global review</text>
      <text x="245" y="702" text-anchor="middle" font-size="17px" opacity="0.6">17th meeting</text>
      <text x="245" y="724" text-anchor="middle" font-size="17px" opacity="0.6">of the COP</text>
      <path class="edge" d="M485 660 L383 660" marker-end="url(#acronym-arrow)"/>
      <text x="430" y="625" text-anchor="middle" font-size="16px" opacity="0.75" font-family="Berkeley Mono, monospace">reviewed</text>
      <text x="430" y="646" text-anchor="middle" font-size="16px" opacity="0.75" font-family="Berkeley Mono, monospace">at</text>
    </g>
    <g v-click>
      <path class="edge" d="M290 350 C 290 410, 320 430, 372 430" marker-end="url(#acronym-arrow)"/>
      <text x="278" y="402" text-anchor="end" font-size="19px" opacity="0.75" font-family="Berkeley Mono, monospace">defines</text>
      <text x="278" y="423" text-anchor="end" font-size="19px" opacity="0.75" font-family="Berkeley Mono, monospace">criteria</text>
      <rect class="node key" x="380" y="385" width="400" height="90" rx="14"/>
      <text x="580" y="428" text-anchor="middle" font-size="40px" font-weight="700">RLE</text>
      <text x="580" y="460" text-anchor="middle" font-size="22px" style="fill:#FFD626">Red List of Ecosystems</text>
      <path class="edge" d="M615 475 L615 552" marker-end="url(#acronym-arrow)"/>
      <text x="601" y="508" text-anchor="end" font-size="19px" opacity="0.75" font-family="Berkeley Mono, monospace">headline indicator A.1 (requested)</text>
      <text x="601" y="531" text-anchor="end" font-size="19px" opacity="0.75" font-family="Berkeley Mono, monospace">complementary indicators (optional)</text>
    </g>
    <g v-click>
      <rect class="node key" x="860" y="385" width="340" height="90" rx="14"/>
      <text x="1030" y="428" text-anchor="middle" font-size="34px" font-weight="700">Ecosystem maps</text>
      <text x="1030" y="460" text-anchor="middle" font-size="22px" style="fill:#FFD626">where ecosystems are</text>
      <path class="edge" d="M860 430 L788 430" marker-end="url(#acronym-arrow)"/>
      <text x="824" y="418" text-anchor="middle" font-size="19px" opacity="0.75" font-family="Berkeley Mono, monospace">input</text>
      <path class="edge" d="M960 475 C 960 520, 735 510, 735 552" marker-end="url(#acronym-arrow)"/>
      <text x="975" y="515" text-anchor="start" font-size="19px" opacity="0.75" font-family="Berkeley Mono, monospace">headline indicator A.2</text>
    </g>
</svg>

<!--
How does international biodiversity policy work?
Get ready for some acronyms...
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
  <span class="statement-sub a-rise" style="--d:0.4s">· <span class="hl">Published 2024</span></span>
  <span class="statement-sub a-rise" style="--d:0.6s">· How to assess an ecosystem's <span class="hl">risk of collapse</span></span></div>

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
id: slide-subterranean-voids
title: Anthropogenic Subterranean Voids
layout: full-bleed
---

<div style="position:absolute; inset:0; overflow:hidden">
  <img src="/images/granite_mountain_vaults.jpg" style="width:100%; height:100%; object-fit:cover" alt="Lit arched tunnel entrances cut into a granite cliff face at dusk" />
  <div style="position:absolute; inset:0; background:linear-gradient(to top, rgba(0,0,0,0.75) 0%, rgba(0,0,0,0) 40%)"></div>
</div>

<div class="a-rise" style="--d:0.4s; position:absolute; left:80px; bottom:64px">
  <div class="statement" style="font-size:3em; line-height:1.1">Anthropogenic Subterranean voids (S2.1)</div>
  <div class="statement-sub muted" style="margin-top:0.4rem">(Mormon Vaults)</div>
</div>

<!--
TODO
-->

---
id: slide-covers
title: Country Assessments
layout: full-bleed
---

<div class="a-rise" style="position:absolute; top:36px; left:0; right:0; text-align:center">
  <span class="statement">Ecosystem Assessment Reports</span>
</div>

<div class="covers" style="height:100%; align-items:center; padding-top:80px; box-sizing:border-box">
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
id: slide-hows-it-going
title: How's It Going?
layout: full-bleed
---

<div class="center-v" style="height:100%; gap:2.4rem">
  <span class="statement a-rise" style="font-size:110px !important; line-height:1.05">So how's it going?</span>
  <span class="statement-sub a-fade" style="--d:1.2s">(i.e. a preview of what will be discussed at COP 17 in two weeks) </span>
</div>

<!--
...
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
<div style="left:448px; top:196px; --d:1.5s" class="fig-card a-fade">
  <img src="/images/buschke_fig1_reporting_status.png" style="width:680px; height:auto; display:block" alt="Figure 1 from Buschke et al.: reporting status for Indicator A.2 across the 196 Parties to the CBD — 31.1% did not submit a 7th National Report, 29.1% did not report A.2, 9.2% incomplete, 30.6% complete" />
  <!-- Highlight the "Complete Indicator A.2 (30.6%)" legend entry, before the Figure 2 highlights -->
  <div class="fig-hl fig-hl-first" style="left:542px; top:12px; width:152px; height:38px"></div>
</div>

<!-- Figure 2, overlapping Figure 1's caption -->
<div style="left:448px; top:490px" class="fig-card fig2" v-click="1">
  <img src="/images/buschke_fig2_sources_disaggregation.png" style="width:680px; height:auto; display:block" alt="Figure 2 from Buschke et al.: (a) data sources and (b) type of disaggregation used by the 78 Parties that reported Indicator A.2 — land cover and ecosystem maps are the most common sources; most Parties reported no disaggregation" />
  <!-- Highlights (positions are the figure's pixels × 680/1456, plus the 12px card padding) -->
  <div class="fig-hl" style="left:40px; top:74px; width:229px; height:30px"></div>
  <div class="fig-hl" style="left:425px; top:86px; width:150px; height:23px"></div>
</div>

<!-- Callout: few national reports are based on ecosystem maps (Buschke et al.: 19 of 196 Parties) -->
<div class="after-fig2" v-click="1" style="--d:1.5s; position:absolute; left:60px; top:520px; width:360px">
  <div style="border:3px solid #FFD626; border-radius:12px; padding:1.1rem 1.3rem; background:rgba(29,35,43,0.92)">
    <div class="statement" style="font-size:2.4em; line-height:1.1"><span class="hl">19</span> of 196</div>
    <div class="statement-sub" style="margin-top:0.4rem">Parties based A.2 on an <span class="hl">ecosystem map</span></div>
  </div>
  <svg viewBox="0 0 70 20" style="position:absolute; left:360px; top:58px; width:70px; height:20px; overflow:visible">
    <path d="M0 10 L58 10" stroke="#FFD626" stroke-width="4" stroke-linecap="round"/>
    <path d="M56 2 L68 10 L56 18 Z" fill="#FFD626"/>
  </svg>
</div>

<!-- Callout: few disaggregate by the Global Ecosystem Typology (Buschke et al.: 15 Parties) -->
<div class="after-fig2" v-click="1" style="--d:3s; position:absolute; left:1180px; top:520px; width:360px">
  <div style="border:3px solid #FFD626; border-radius:12px; padding:1.1rem 1.3rem; background:rgba(29,35,43,0.92)">
    <div class="statement" style="font-size:2.4em; line-height:1.1"><span class="hl">15</span> of 196</div>
    <div class="statement-sub" style="margin-top:0.4rem">Parties disaggregated A.2 by the <span class="hl">GET</span></div>
  </div>
  <svg viewBox="0 0 150 20" style="position:absolute; left:-152px; top:61px; width:150px; height:20px; overflow:visible">
    <path d="M150 10 L12 10" stroke="#FFD626" stroke-width="4" stroke-linecap="round"/>
    <path d="M14 2 L2 10 L14 18 Z" fill="#FFD626"/>
  </svg>
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
/* Highlights: the Figure 1 legend entry fades in at 2.6s; Figure 2's fade in shortly after its click */
.fig-hl {
  opacity: 0;
  position: absolute;
  border: 3px solid #FFD626;
  border-radius: 6px;
  background: rgba(255, 214, 38, 0.18);
  box-shadow: 0 0 12px rgba(255, 214, 38, 0.6);
}
.fig-hl.fig-hl-first {
  animation: fade-in 0.6s ease-out 2.6s both; /* shortly after Figure 1 appears */
}
.fig2:not(.slidev-vclick-hidden) .fig-hl {
  animation: fade-in 0.6s ease-out 0.8s both;
}
/* Callouts follow Figure 2's click, one after the other (--d set on each) */
.after-fig2 { opacity: 0; }
.after-fig2:not(.slidev-vclick-hidden) {
  animation: fade-in 0.6s ease-out var(--d, 0s) both;
}
</style>

<!--
Source of images: Buschke et al., "**Reporting on the extent of natural ecosystems under the Kunming-Montreal Global Biodiversity Framework**"
- Available on eco-evo-archive
- 29% of countries reported on A.2 (extent of natural ecosystems)
- Only 19 countries based their estimate on an ecosystem map
- Only 15 countries used GET
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
id: slide-architecture
title: Architecture
layout: full-bleed
---

<ArchitectureDiagram />

<!--
TODO
-->

---
id: slide-github-org
title: RLE Assessment on GitHub
layout: full-bleed
---

<div class="center-v a-rise" style="height:100%">
  <a href="https://github.com/rle-assessment" target="_blank" class="frame">
    <img src="/images/github_rle_assessment.jpg" style="height:700px; width:auto; display:block" alt="The RLE Assessment GitHub organization page, with a README describing tools for building IUCN Red List of Ecosystems assessment reports" />
  </a>
</div>

<a href="https://github.com/rle-assessment" target="_blank" style="position:absolute; bottom:40px; right:80px" class="mono muted">github.com/rle-assessment</a>

<!--
TODO
-->

---
id: slide-auth-dance
title: The Hard Part
layout: full-bleed
---

<AuthDance />

<!--
The hardest part isn't the geospatial computation: it's setting up authentication so Google (Earth Engine / Cloud), GitHub (Actions), the CDN, and object storage can all work together.
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
id: slide-colombia-site (screenshot)
title: Colombia Assessment Site (screenshot)
layout: full-bleed
---

<div style="position:absolute; inset:0; overflow:hidden">
  <img src="/images/demo/home.png" style="width:100%; height:100%; object-fit:cover; object-position:top" alt="Wildlife Insights dashboard" />
</div>

<!--
Wildlife Insights is an AI-powered platform that helps researchers process and share camera trap data at scale — using machine learning to identify species in images, reducing the manual work from months to hours.
-->

---
id: slide-architecture-recap
title: Architecture (recap)
layout: full-bleed
---

<ArchitectureDiagram no-clicks highlight-maps />

<!--
Repeat of the architecture slide, fully revealed.
-->

---
id: slide-need-maps
title: We Need Ecosystem Maps
layout: full-bleed
---

<div class="center-v" style="height:100%; gap:2.2rem">
  <span class="statement a-rise" style="font-size:120px !important; line-height:1.05; text-align:center">We need <span class="hl">ecosystem maps</span></span>
  <span v-click class="statement-sub" style="font-size:56px !important">When do we need them?</span>
  <span v-click class="statement hl" style="font-size:220px !important; line-height:1">NOW!</span>
</div>

<!--
TODO
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

<div style="position:absolute; left:700px; width:860px; top:130px" class="stats stats-ralign">
  <div class="a-rise" style="--d:0.4s"><span class="num">87</span><span class="unit">ecosystem types</span></div>
  <div class="a-rise" style="--d:0.8s"><span class="num">460,350</span><span class="unit">ecosystem polygons</span></div>
  <div class="a-rise" style="--d:1.2s"><span class="num">1.7 GB</span><span class="unit">as GeoParquet</span></div>
  <div class="a-rise unit" style="--d:1.6s; display:block; margin:1.2rem 0 0">Also rasterized to 10m...</div>
  <div class="a-rise" style="--d:2s"><span class="num">520 MB</span><span class="unit">as Cloud-optimized GeoTIFF</span></div>
</div>

<style>
/* Right-align the big numbers in a fixed column so their right edges line up */
.stats-ralign .num { display: inline-block; width: 480px; text-align: right; }
.stats-ralign > div { white-space: nowrap; }
</style>

<!--
TODO
-->

---
id: slide-ecosystems-atlas
title: Global Ecosystems Atlas
layout: full-bleed
---

<div style="position:absolute; left:100px; width:560px; top:0; bottom:0; display:flex; flex-direction:column; justify-content:center; gap:1.4rem">
  <span class="eyebrow a-rise">Group on Earth Observations</span>
  <span class="statement a-rise" style="--d:0.2s; font-size:3.4em">Global Ecosystems Atlas</span>
  <span class="statement-sub a-rise" style="--d:0.4s">Helping countries develop the capacity to produce <span class="hl">ecosystem maps</span> with tools and trainings</span>
  <a href="https://doi.org/10.32942/X22Q3M" target="_blank" class="mono muted a-fade" style="--d:0.8s">Murray et al. 2026 · doi.org/10.32942/X22Q3M</a>
</div>

<div style="position:absolute; right:80px; top:0; bottom:0; display:flex; align-items:center" class="a-rise">
  <a href="https://www.globalecosystemsatlas.org/" target="_blank" class="frame">
    <img src="/images/global_ecosystems_atlas.jpg" style="width:780px; height:auto; display:block" alt="Home page of the Global Ecosystems Atlas: a global partnership advancing ecosystem intelligence" />
  </a>
</div>

<!-- Partner logos, as shown on globalecosystemsatlas.org -->
<div class="a-fade" style="--d:1.2s; position:absolute; left:0; right:0; bottom:40px; display:flex; flex-direction:column; align-items:center; gap:10px">
  <span class="mono muted" style="font-size:0.75em; letter-spacing:0.08em; align-self:flex-start; margin-left:250px">Powered by a world-class technical consortium and partners</span>
  <div style="display:flex; align-items:center; gap:48px; background:#f1f1f1; border-radius:12px; padding:16px 36px">
    <img src="/images/atlas_partners/cbd.png" alt="Convention on Biological Diversity" style="height:44px; width:auto; display:block" />
    <img src="/images/atlas_partners/iucn.png" alt="IUCN" style="height:44px; width:auto; display:block" />
    <img src="/images/atlas_partners/jcu.svg" alt="James Cook University" style="height:44px; width:auto; display:block" />
    <img src="/images/atlas_partners/esa.png" alt="European Space Agency" style="height:44px; width:auto; display:block" />
    <img class="partner-hl" src="/images/atlas_partners/google.png" alt="Google" style="height:44px; width:auto; display:block" />
    <img class="partner-hl" src="/images/atlas_partners/ai2.png" alt="Allen Institute for AI" style="height:44px; width:auto; display:block" />
    <img src="/images/atlas_partners/esri.png" alt="Esri" style="height:44px; width:auto; display:block" />
  </div>
</div>

<!-- Callout: Google and Ai2 contribute geospatial embeddings -->
<div class="a-fade" style="--d:3s; position:absolute; left:860px; top:668px; border:3px solid #FFD626; border-radius:12px; padding:0.35rem 1.2rem; background:rgba(29,35,43,0.95)">
  <span class="statement hl" style="font-size:2em; line-height:1.1">geo embeddings!</span>
</div>
<svg class="a-fade" viewBox="0 0 1600 900" style="--d:3s; position:absolute; inset:0; width:100%; height:100%; pointer-events:none">
  <path d="M925 725 L900 768" stroke="#FFD626" stroke-width="4" stroke-linecap="round"/>
  <path d="M893 780 L893 765 L907 772 Z" fill="#FFD626"/>
  <path d="M1035 725 L1060 768" stroke="#FFD626" stroke-width="4" stroke-linecap="round"/>
  <path d="M1067 780 L1053 772 L1067 765 Z" fill="#FFD626"/>
</svg>

<style>
/* Highlight Google and Ai2 in the partner strip, shortly after it appears */
.partner-hl {
  outline: 6px solid transparent;
  outline-offset: 8px;
  border-radius: 8px;
  animation: partner-hl 0.6s ease-out 2s both, partner-pulse 1.6s ease-in-out 2.6s 3;
}
@keyframes partner-hl {
  from { outline-color: transparent; box-shadow: 0 0 0 0 rgba(255,214,38,0); transform: scale(1); }
  to   { outline-color: #FFD626; box-shadow: 0 0 34px 18px rgba(255,214,38,0.8); transform: scale(1.12); }
}
@keyframes partner-pulse {
  0%, 100% { box-shadow: 0 0 34px 18px rgba(255,214,38,0.8); }
  50%      { box-shadow: 0 0 52px 28px rgba(255,214,38,1); }
}
</style>

<!--
Preprint: Murray et al., "The Global Ecosystems Atlas: comprehensive and systematic mapping of Earth's ecosystems", EcoEvoRxiv, posted 31 July 2026 — https://doi.org/10.32942/X22Q3M (https://ecoevorxiv.org/repository/view/14123/)
Open-access dataset of 110 ecosystem functional groups, 25 biomes, and 10 realms; supports monitoring aligned with the KMGBF.
Site: https://www.globalecosystemsatlas.org/
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
id: slide-whats-next
title: What's Next
layout: full-bleed
---

<div style="position:absolute; left:100px; width:820px; top:0; bottom:0; display:flex; flex-direction:column; justify-content:center; gap:1.6rem">
  <span class="statement a-rise" style="font-size:4em">What's next</span>
  <ul class="lessons" style="margin-top:0.6rem; font-size:1.7em">
    <li v-click.fade>Prototype → <span class="hl">IUCN Red List of Ecosystems</span> team</li>
    <li v-click.fade>RLE calculations from Python → <span class="hl">Rust</span></li>
    <li v-click.fade>Teach countries the <span class="hl">Portolan</span> dance</li>
  </ul>
</div>

<div class="a-fade" style="--d:0.6s; position:absolute; right:40px; top:60px; width:700px; height:760px">
  <PortolanDisco :start="$clicks >= 3" />
</div>

<style>
/* Bullets start faded and become bright on their click */
#slide-whats-next .lessons li { transition: opacity 0.6s ease-out; }
#slide-whats-next .lessons li.slidev-vclick-fade { opacity: 0.22; }
</style>

<!--
Click 1–3: each bullet brightens. Click 3 (Portolan) also starts the dance floor sequence.
-->

---
id: slide-thanks
title: Thank You
layout: full-bleed
background: /images/hero_forest_coast.jpg
---

<div class="center-v deep-copy" style="height:100%; gap:1.2rem; font-size:1.8rem">
  <span class="statement a-rise" style="font-size:3em; margin-bottom:1rem">Thank you</span>
  <a href="https://iucnrle.org/">iucnrle.org</a>
  <a href="https://github.com/rle-assessment">github.com/rle-assessment</a>
  <a href="https://tylere.github.io/rle-tyler-colombia/">tylere.github.io/rle-tyler-colombia</a>
  <div class="a-fade" style="--d:0.6s; margin-top:2.5rem; padding-top:1.8rem; border-top:1px solid rgba(242,244,246,0.25); display:flex; flex-direction:column; align-items:center; gap:0.6rem; font-size:0.8em">
    <span style="font-weight:700; font-size:1.2em; color:#F2F4F6">Tyler Erickson</span>
    <span class="muted"><span class="hl">VorGeo</span> · Founder &nbsp;|&nbsp; <span class="hl">Radiant Earth</span> · CTO</span>
    <span class="mono"><a href="https://www.linkedin.com/in/tylere">linkedin.com/in/tylere</a> · <a href="https://github.com/tylere">github.com/tylere</a> · <a href="https://www.analyze.earth">analyze.earth</a></span>
  </div>
</div>

<!--
TODO
-->
