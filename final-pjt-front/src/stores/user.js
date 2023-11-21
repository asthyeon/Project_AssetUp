import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useAddressStore } from '@/stores/address'

export const useUserStore = defineStore('user', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()
  const name = ref(null)
  const user = ref({})
  const addressStore = useAddressStore()

  // 회원가입 기능
  const signUp = function (payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    const nickname = payload.nickname
    // const email = payload.email
    const age = payload.age
    const salary = payload.salary
    const money = payload.money

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, nickname, age, salary, money
      }
    })
      .then(res => {
        console.log(res.data);
        const password = password1
        // 회원가입 하면 로그인 상태 유지하기
        console.log(username, password)
        logIn({ username, password })
      })
      .catch(err => console.log(err))
  }

  // 로그인 기능
  const logIn = function (payload) {
    console.log(payload)
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
        // accessToken 받아오기
        addressStore.getToken() 
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

  // 회원 정보 수정
  const userUpdate = function (payload) {
    const newData = {
      username: payload.username,
      email: payload.email,
      nickname: payload.nickname,
      age: payload.age,
      salary: payload.salary,
      money: payload.money
    }
  
    axios({
      method: 'put',
      url: `${API_URL}/accounts/update-user/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
      data: newData,
    })
      .then((res) => {
        user.value = res.data
        console.log(res.data)
        console.log('회원정보 수정 완료!!');
      })
      .then(() => {
        router.push({name:'profile'})
      })
      .catch((err) => console.log(err));
  }

  // 상품 구독
  const unsubscribe = function (finPrdtCd) {
    // 기존 상품 구독 문자열
    const existingProducts = user.value.financial_products || ''

    // 이미 구독한 상품인 경우 해당 상품 제거
    if (existingProducts.includes(finPrdtCd)) {
      const updatedProducts = existingProducts.split(',').filter(productCode => productCode !== finPrdtCd).join(',')
      console.log('구독을 해제합니다.')

      axios({
        method: 'put',
        url: `${API_URL}/accounts/update-user/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
        data: { financial_products: updatedProducts },
      })
        .then((res) => {
          user.value = res.data
          console.log(res.data)
        })
        .catch((err) => console.log(err))
    }}
  const subscribe = function (finPrdtCd) {
    const existingProducts = user.value.financial_products || ''

    // 없는 상품인 경우 새로 구독하기
    const newFinPrdtCd = existingProducts ? `${existingProducts},${finPrdtCd}` : finPrdtCd

    axios({
      method: 'put',
      url: `${API_URL}/accounts/update-user/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
      data: { financial_products: newFinPrdtCd },
    })
      .then((res) => {
        user.value = res.data;
        console.log(res.data);
        console.log('상품 구독 완료');
      })
      .catch((err) => console.log(err));
  }

  return { signUp, logIn, logOut, userUpdate, subscribe, unsubscribe, isLogin, token, name, user }
}, { persist: true })
