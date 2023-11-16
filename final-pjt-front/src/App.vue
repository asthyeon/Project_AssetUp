
<template>
  <header>
    <nav>
      <RouterLink :to="{name:'main'}">Home</RouterLink> |
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import MainView from '@/views/MainView.vue'
</script>

<style scoped>

</style>
