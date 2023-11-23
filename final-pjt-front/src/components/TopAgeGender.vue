<template>
  <div>
    <!-- 나이, 성별 Top 3 -->
    <h2>{{ ageRange }} {{ genderString }} Top3</h2>
    <div v-for="product in recommendStore.rankedProductsList">
      {{ product.product.kor_co_nm }}
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRecommendStore } from '@/stores/recommend'
import { useUserStore } from '@/stores/user'
import { useFinanceStore } from '@/stores/finance'

const userStore = useUserStore()
const recommendStore = useRecommendStore()

const userAge = userStore.user.age;

recommendStore.rankingProdut({age:userStore.user.age, gender:userStore.user.gender})

// 나이 변환
let ageRange;

if (userAge < 10) {
  ageRange = '10세 미만';
} else if (userAge < 20) {
  ageRange = '10대';
} else if (userAge < 30) {
  ageRange = '20대';
} else if (userAge < 40) {
  ageRange = '30대';
} else if (userAge < 50) {
  ageRange = '40대';
} else if (userAge < 60) {
  ageRange = '50대';
} else {
  ageRange = '60세 이상';
}
// 성별 변환
const userGender = userStore.user.gender;

let genderString;

if (userGender === 'M') {
  genderString = '남성';
} else if (userGender === 'F') {
  genderString = '여성';
} else {
  genderString = '기타'; // 다른 경우에 대한 처리를 원하는 대로 설정할 수 있습니다.
}

</script>

<style scoped>

</style>