<script setup lang="ts">
import { computed } from 'vue'
import { useNav, useSlideContext } from '@slidev/client'

const { $page } = useSlideContext()
const { currentPage } = useNav()
const isActive = computed(() => currentPage.value === $page.value)
</script>

<template>
  <div class="pile" :class="{ active: isActive }">
    <span class="chip" style="left:40px; top:40px; --r:-4deg; --d:0.3s">Python environment</span>
    <span class="chip" style="left:470px; top:10px; --r:3deg; --d:0.6s">GitHub account</span>
    <span class="chip" style="left:880px; top:50px; --r:-2deg; --d:0.9s">Google Cloud project</span>
    <span class="chip" style="left:120px; top:170px; --r:5deg; --d:1.2s">gcloud auth login</span>
    <span class="chip" style="left:620px; top:190px; --r:-6deg; --d:1.5s">application-default login</span>
    <span class="chip warn" style="left:1230px; top:160px; --r:8deg; --d:1.8s">MFA</span>
    <span class="chip warn" style="left:60px; top:320px; --r:-3deg; --d:2.1s">IAM roles</span>
    <span class="chip" style="left:380px; top:350px; --r:4deg; --d:2.4s">service account</span>
    <span class="chip" style="left:860px; top:330px; --r:-5deg; --d:2.7s">Earth Engine registration</span>
    <span class="chip warn" style="left:200px; top:490px; --r:6deg; --d:3.0s">billing</span>
    <span class="chip" style="left:520px; top:520px; --r:-2deg; --d:3.3s">bucket CORS</span>
    <span class="chip" style="left:900px; top:490px; --r:3deg; --d:3.6s">GitHub secrets</span>
    <span class="chip warn" style="left:1200px; top:560px; --r:-7deg; --d:3.9s">Pages settings</span>
  </div>
</template>
