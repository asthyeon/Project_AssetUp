<template>
    <div>
      <h1>금융상품 상세 정보</h1>
      <div v-if="userStore.isLogin">
            <!-- 구독 중인 상품인 경우 -->
            <div v-if="userProductsArray.includes(product.fin_prdt_cd)" >
                <p>이미 구독 중인 상품입니다.</p>
                <button @click="updateUser(false)">해제하기</button>
            </div>
            <!-- 구독할 수 있는 상품인 경우 -->
            <div v-else>
                <p>가입 대상입니다.</p>
                <button @click="updateUser(true)">가입하기</button>
            </div>        </div>
        <p>상품 정보</p>
        <div>
            <p>공시제출월 : {{ product.dcls_month }}</p>
            <p>금융회사명 : {{ product.kor_co_nm }}</p>
            <p>상품명 : {{ product.fin_prdt_nm }}</p>
            <p>가입제한 : {{ JOIN_DENY_CHOICES[product.join_deny] }}</p>
            <p>가입방법 : {{ product.join_way }}</p>
            <p>우대조건 :</p>
            <p>{{ product.spcl_cnd }}</p>
            <p v-html="formatSpecialConditions(product.spcl_cnd)"></p>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useFinanceStore } from '@/stores/finance'
import { useUserStore } from '@/stores/user'
import { useRoute, useRouter } from 'vue-router'

const financeStore = useFinanceStore()
const userStore = useUserStore()

const route = useRoute()
const finPrdtCd = ref('')
const product = ref({})

// 현재 금융상품코드
finPrdtCd.value = route.params.fin_prdt_cd
// 단일 상품 조회
financeStore.getSavingProductDetail(finPrdtCd.value)
// 단일 상품의 옵션 목록 조회
financeStore.getSavingProductOptions(finPrdtCd.value)
// 단일 상품 정보 저장
product.value = financeStore.savingProduct
// 가입제한 정보
const JOIN_DENY_CHOICES = {
    1: '제한 없음',
    2: '서민전용',
    3: '일부제한',
}
// 우대조건 줄바꿈 함수
const formatSpecialConditions = (spclCnd) => {
  const formattedConditions = spclCnd.replace('\n', '<br>')
  console.log(formattedConditions)
  return formattedConditions
}
// 상품 구독하기
const updateUser = (isSubscribe) => {
  if (isSubscribe) {
    // 가입하기
    userStore.subscribe(product.value.fin_prdt_cd);
  } else {
    // 해제하기
    userStore.unsubscribe(product.value.fin_prdt_cd);
  }
  // 유저의 구독 상품 목록 갱신
  userProductsArray.value = userStore.user.financial_products.split(',');
}
// 유저의 구독 상품 목록
const userProductsArray = ref(userStore.user.financial_products.split(','))
</script>

<style scoped>

</style>