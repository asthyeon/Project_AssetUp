<template>
  <div id="app">
    <KakaoMap />
  </div>
</template>

<script>
import KakaoMap from "@/components/KakaoMap.vue";

export default {
  name: "App",
  components: {
    KakaoMap,
  },
};
</script>