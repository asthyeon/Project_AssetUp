<template>
    <div>
        <div>
            <h1>금융상품 상세 정보</h1>
            <button @click="updateUser">가입하기</button>
        </div>
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

finPrdtCd.value = route.params.fin_prdt_cd

financeStore.getSavingProductDetail(finPrdtCd.value)
financeStore.getSavingProductOptions(finPrdtCd.value)

product.value = financeStore.savingProduct

const JOIN_DENY_CHOICES = {
    1: '제한 없음',
    2: '서민전용',
    3: '일부제한',
}

const formatSpecialConditions = (spclCnd) => {
  // \n를 기준으로 줄바꿈을 추가
  const formattedConditions = spclCnd.replace('\n', '<br>')
  console.log(formattedConditions)
  return formattedConditions
}

const updateUser = () => {
    console.log('가입하기')
  userStore.subscribe(product.value.fin_prdt_cd)
}
</script>

<style scoped>

</style>