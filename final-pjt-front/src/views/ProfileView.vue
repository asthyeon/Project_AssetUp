<template>
  <div>
    <header>
      <h1>{{ user.username }} 님의 프로필 페이지</h1>
    </header>

    <div>
      <p>기본 정보 수정</p>
      <p>포트폴리오 수정</p>
      <p>상품 추천 받기</p>
    </div>

    <div>
      <div>
        <h2>기본 정보 수정</h2>
      </div>
      <div>
        <p>회원 번호 : {{ user.id }}</p>
        <p>ID : {{ user.username }}</p>
        <p>
          <span>Email : </span>
          <span v-if="!user.email">이메일을 수정해주세요</span>
          <span v-else>{{ user.email }}</span>
          <button @click="goUpdate">수정하기</button>
        </p>
        <p>
          <span>Nickname : {{ user.nickname }}</span>
          <button @click="goUpdate">수정하기</button>
        </p>
        <p>
          <span>나이 : {{ user.age }}</span>
          <button @click="goUpdate">수정하기</button>
        </p>
        <p>
          현재 가진 금액 : {{ user.money }}
          <button @click="goUpdate">수정하기</button>
        </p>
        <p>
          연봉 : {{ user.salary }}
          <button @click="goUpdate">수정하기</button>
        </p>
        <div>
          <strong>가입 상품 목록</strong>
          <ul v-if="user.financial_products && user.financial_products.length > 0">
            <li v-for="product in user_products" :key="product.id">
              {{ product.product_name }} - {{ product.product_code }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'
import { useFinanceStore } from '@/stores/finance'

const userStore = useUserStore()
const financeStore = useFinanceStore()
const allProducts = ref([])

const user_products = ref([])

onMounted(async () => {
  await financeStore.getDepositProducts()
  await financeStore.getSavingProducts()
  
  allProducts.value = [
      ...financeStore.depositProductList,
      ...financeStore.savingProductList
    ]

  console.log(allProducts.value);

  user_products.value = userStore.user.financial_products
    .split(',')
    .map(finPrdtCd => findProductByCode(finPrdtCd))
    .filter(product => product !== null)

  console.log(user_products.value)
})

const user = ref('')

user.value = userStore.user

const router = useRouter()

const goUpdate = function () {
  router.push({name:'update'})
}


const findProductByCode = function (finPrdtCd) {
  return allProducts.value.find(product => product.fin_prdt_cd === finPrdtCd) || null
}

</script>

<style scoped>

</style>