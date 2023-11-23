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
  // 추천 업데이트
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
    // 추천 상품 요청
    rankingProdut(payload)
  }

  const calculateAssetGrowthRate = (finPrdtCd, saveTerm) => {
    // 1. finPrdtCd에 해당하는 상품 찾기
    financeStore.getAllProducts()

    const targetProduct = financeStore.allProductList.find(product => product.product.fin_prdt_cd === finPrdtCd)
    // 2. 예금인지 적금인지 체크
    const intr_rate_type_nm = ref('')
    if (targetProduct.product.fin_prdt_nm.includes('예금')) {
      // 2-1. 예금이면
      intr_rate_type_nm.value = '단리'
    } else {
      intr_rate_type_nm.value = '복리'
    }
    
    // 3. 선택한 예치 기간에 해당하는 옵션 찾기
    const options = targetProduct.options    
    const selectedOption = options.find(option => option.save_trm === saveTerm)

    // 만약 옵션이 없으면
    if (!selectedOption) {
      console.error(`No option found for the selected deposit period: ${saveTerm}`)
      return null
    }
    // 저축 금리, 우대금리
    const interestRate = selectedOption.intr_rate
    const interestRate2 = selectedOption.intr_rate2

    return {intr_rate_type_nm, interestRate, interestRate2}
  }

  return { rankedProductsList, rankingProdut, updateRecommendation, calculateAssetGrowthRate }
}, { persist: true })
