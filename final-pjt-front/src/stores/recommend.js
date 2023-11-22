import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useAddressStore } from '@/stores/address'
 
export const useRecommendStore = defineStore('recommend', () => {
  const rankedProductsList = ref({})

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
        rankedProductsList.value = res.data
        console.log('상품 추천이 완료되었습니다.')
    }).catch(err => console.log(err))
  }
  return { rankedProductsList, rankingProdut }
}, { persist: true })
