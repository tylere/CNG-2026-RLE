<template>
  <div class="cards">
    <div v-click class="card">
      <h3>One command</h3>
      <pre><code>uv run …/init_repo.py \
  --country-name Colombia
pixi shell</code></pre>
    </div>
    <div v-click class="card">
      <h3>Fork a template</h3>
      <svg class="big-icon" viewBox="0 0 120 150" aria-label="Fork icon">
        <g fill="none" stroke="#FFD626" stroke-width="7" stroke-linecap="round">
          <circle cx="25" cy="22" r="14"/><circle cx="95" cy="22" r="14"/><circle cx="60" cy="128" r="14"/>
          <path d="M25 36 V60 Q25 78 60 78 Q95 78 95 60 V36 M60 78 V114"/>
        </g>
      </svg>
    </div>
    <div v-click class="card">
      <h3>Config, not code</h3>
      <pre><code>ecosystem_source:
  data: …/colombia.parquet
  ecosystem_name_column:
    ecos_general</code></pre>
    </div>
  </div>
</template>
