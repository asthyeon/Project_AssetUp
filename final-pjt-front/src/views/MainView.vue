<template>
  <div>
    <h1>메인 페이지</h1>
    <hr>
    <div 
      v-for="dp in store.topDps"
      :key="dp.fin_prdt_cd"
    >
      <p>
        {{ dp.fin_prdt_nm }}
      </p>
    </div>
    <hr>
    <div 
      v-for="sp in store.topSps"
      :key="sp.fin_prdt_cd"
    >
      <p>
        {{ sp.fin_prdt_nm }}
      </p>
    </div>
    <hr>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useHomeStore } from '@/stores/home';

const store = useHomeStore()

onMounted(() => {
  store.getAll()
})

</script>

<style scoped>

</style>