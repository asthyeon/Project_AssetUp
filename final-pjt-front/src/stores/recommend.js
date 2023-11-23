import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useAddressStore } from '@/stores/address'
import { useUserStore } from '@/stores/user'
import { useFinanceStore } from '@/stores/finance'
 
export const useRecommendStore = defineStore('recommend', () => {
  const rankedProductsList = ref([])
  const userStore = useUserStore()
  const financeStore = useFinanceStore()

  // 상품 순위 필터링 후 반환
  const rankingProdut = (payload) => {
    console.log(payload);
    axios({
        method: 'post',
        url: `http://127.0.0.1:8000/finances/filter-user/`,
        data: payload,
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
    }).then((res) => {
      const tempProducts = ref(res.data.map(entry => entry[0]))

      const filteredProductCodes = tempProducts.value.map(productCode => productCode)
      
      financeStore.getAllProducts()
      const allProducts = ref(financeStore.allProductList)

      rankedProductsList.value = filteredProductCodes.map(productCode => {
        return allProducts.value.find(product => product.product.fin_prdt_cd === productCode) || null;
      })

      console.log('상품 추천이 완료되었습니다.')
    }).catch(err => console.log(err))
  }

  const updateRecommendation = (selectedOptions) => {
    const payload = {}
  
    if (selectedOptions.age) {
      payload.age = userStore.user.age
    }
    if (selectedOptions.gender) {
      payload.gender = userStore.user.gender
    }
    if (selectedOptions.mbti) {
      payload.mbti = userStore.user.mbti
    }
    if (selectedOptions.salary) {
      payload.salary = userStore.user.salary
    }
    // 필터링된 상품 리스트 업데이트
  
    // 추천 상품 요청
    rankingProdut(payload)
  }

  return { rankedProductsList, rankingProdut, updateRecommendation }
}, { persist: true })
