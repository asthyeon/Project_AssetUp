import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import axios from 'axios'

export const useBoardStore = defineStore('board', () => {
  const userStore = useUserStore()
  console.log(userStore.token);
  const token = userStore.token
  const board_articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()

  // 로그인 유무 확인
  const isLogin = computed(() => {
    if (token === null) {
      return false
    } else {
      return true
    }
  })

  // DRF에 board_article 조회 요청을 보내는 action
  const getBoardArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/board-articles/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
      .then((res) =>{
        // console.log(res)
        board_articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }


  return { isLogin, board_articles, getBoardArticles, API_URL, token }
}, { persist: true })
