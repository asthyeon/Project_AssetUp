<template>
  <div id="app" class="">
    <KakaoMap class="kakao-map" />
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

<style scoped>
.app-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #eafce1; /* 밝은 초록색 배경 색상 */
}

.kakao-map {
  width: 80%;
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
  border: 2px solid #4caf50; /* 초록색 테두리 색상 */
  border-radius: 10px;
  overflow: hidden;
}
</style>
