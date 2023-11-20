import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()
  const name = ref(null)
  const user = ref({})

  // 회원가입 기능
  const signUp = function (payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then(res => {
        const password = password1
        // 회원가입 하면 로그인 상태 유지하기
        logIn({ username, password })
      })
      .catch(err => console.log(err))
  }

  // 로그인 기능
  const logIn = function (payload) {
    const username = payload.username
    const password = payload.password
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then(res => {
        token.value = res.data.key
        name.value = username
        // 유저 정보를 받아오기
        axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`,
          headers: {
            Authorization: `Token ${token.value}`
          }
        })
        .then(res => {
          user.value = res.data
          console.log(res.data);
          // 로그인 후 메인페이지로 이동
          router.push({name: 'main'})
        })
      })
      .catch(err => console.log(err))
  }

  // 로그아웃 함수
  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(() => {
        // 로그아웃 성공 시 로컬 상태 초기화
        token.value = null
        router.push({ name: 'login'})
      })
      .catch(err => console.log(err.response.data))
  }

  // 로그인 여부
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  return { signUp, logIn, logOut, isLogin, token, name, user }
}, { persist: true })
