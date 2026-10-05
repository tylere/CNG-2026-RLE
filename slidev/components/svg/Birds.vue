<template>
  <g class="birds">
    <g class="bird-fly rtl" style="--d:18.3s; --t:93s; --y:227px"><g class="bob" style="--b:3.0s; --bob:15px"><g transform="translate(0.0 0.0)"><g class="flap" style="animation-duration:0.42s; animation-delay:-0.10s"><path class="bird" d="M-17.6 0 Q-8.8 -9.5 0 0 Q8.8 -9.5 17.6 0"/></g></g><g transform="translate(-38.3 0.6)"><g class="flap" style="animation-duration:0.42s; animation-delay:-0.31s"><path class="bird" d="M-18.6 0 Q-9.3 -10.0 0 0 Q9.3 -10.0 18.6 0"/></g></g></g></g>
    <g class="bird-fly rtl" style="--d:16.1s; --t:65s; --y:228px"><g class="bob" style="--b:3.1s; --bob:12px"><g transform="translate(0.0 0.0)"><g class="flap" style="animation-duration:0.51s; animation-delay:-0.10s"><path class="bird" d="M-25.4 0 Q-12.7 -13.7 0 0 Q12.7 -13.7 25.4 0"/></g></g><g transform="translate(-51.7 -9.9)"><g class="flap" style="animation-duration:0.46s; animation-delay:-0.24s"><path class="bird" d="M-25.0 0 Q-12.5 -13.5 0 0 Q12.5 -13.5 25.0 0"/></g></g></g></g>
    <g class="bird-fly" style="--d:41.9s; --t:79s; --y:271px"><g class="bob" style="--b:4.1s; --bob:13px"><g transform="translate(0.0 0.0)"><g class="flap" style="animation-duration:0.39s; animation-delay:-0.44s"><path class="bird" d="M-21.6 0 Q-10.8 -11.6 0 0 Q10.8 -11.6 21.6 0"/></g></g><g transform="translate(-38.8 10.2)"><g class="flap" style="animation-duration:0.41s; animation-delay:-0.02s"><path class="bird" d="M-22.6 0 Q-11.3 -12.2 0 0 Q11.3 -12.2 22.6 0"/></g></g><g transform="translate(-73.3 6.8)"><g class="flap" style="animation-duration:0.41s; animation-delay:-0.05s"><path class="bird" d="M-25.9 0 Q-12.9 -14.0 0 0 Q12.9 -14.0 25.9 0"/></g></g></g></g>
    <g class="bird-fly" style="--d:10.3s; --t:67s; --y:262px"><g class="bob" style="--b:3.4s; --bob:12px"><g transform="translate(0.0 0.0)"><g class="flap" style="animation-duration:0.35s; animation-delay:-0.45s"><path class="bird" d="M-19.2 0 Q-9.6 -10.4 0 0 Q9.6 -10.4 19.2 0"/></g></g><g transform="translate(-77.4 -13.2)"><g class="flap" style="animation-duration:0.48s; animation-delay:-0.02s"><path class="bird" d="M-21.9 0 Q-11.0 -11.8 0 0 Q11.0 -11.8 21.9 0"/></g></g></g></g>
  </g>
</template>

<style scoped>
.bird {
  fill: none;
  stroke: #F2F4F6;
  stroke-width: 4;
  stroke-linecap: round;
}

.bird-fly {
  opacity: 0;
  animation: bird-fly var(--t, 10s) linear var(--d, 0s) infinite both;
  animation-play-state: var(--play-state, paused);
}

.bird-fly.rtl {
  animation-name: bird-fly-rtl;
}

.flap {
  transform-box: fill-box;
  transform-origin: 50% 50%;
  animation: flap 0.35s ease-in-out infinite alternate;
  animation-play-state: var(--play-state, paused);
}

.bob {
  animation: bob var(--b, 3s) ease-in-out infinite alternate;
  animation-play-state: var(--play-state, paused);
}

@keyframes bird-fly {
  0%          { opacity: 1; transform: translate(-400px, var(--y)); }
  60%         { opacity: 1; transform: translate(2000px, calc(var(--y) - 60px)); }
  60.1%, 100% { opacity: 0; transform: translate(2000px, calc(var(--y) - 60px)); }
}

@keyframes bird-fly-rtl {
  0%          { opacity: 1; transform: translate(2000px, var(--y)); }
  60%         { opacity: 1; transform: translate(-400px, calc(var(--y) - 40px)); }
  60.1%, 100% { opacity: 0; transform: translate(-400px, calc(var(--y) - 40px)); }
}

@keyframes bob {
  from { transform: translateY(0); }
  to   { transform: translateY(var(--bob, 10px)); }
}

@keyframes flap {
  from { transform: scaleY(1); }
  to   { transform: scaleY(-0.5); }
}
</style>
