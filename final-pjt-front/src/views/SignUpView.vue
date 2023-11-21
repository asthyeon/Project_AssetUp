<template>
  <div>
    <h1>회원가입 페이지</h1>
    <!-- 회원가입 form -->
    <form @submit.prevent="signUp">
      <label for="username">아이디 : </label>
      <input type="text" id="username" v-model.trim="username"><br>
      <label for="password1">비밀번호 : </label>
      <input type="password" id="password1" v-model.trim="password1"><br>
      <label for="password2">비밀번호 확인 </label>
      <input type="password" id="password2" v-model.trim="password2"><br>
      <label for="nickname">별명 </label>
      <input type="nickname" id="nickname" v-model.trim="nickname"><br>

      <label for="gender">성별</label><br>
      <input type="radio" id="male" value="M" v-model="gender">
      <label for="male">남자</label><br>
      <input type="radio" id="female" value="F" v-model="gender">
      <label for="female">여자</label><br>

      <label for="age">나이 </label>
      <input type="age" id="age" v-model.trim="age"><br>
      <label for="address">주소 </label>
      <input type="address" id="address" v-model.trim="address"><br>
      <label for="salary">연봉 </label>
      <input type="salary" id="salary" v-model.trim="salary"><br>
      <label for="money">현자산 </label>
      <input type="money" id="money" v-model.trim="money"><br>
      <label for="mbti">MBTI </label>
      <input type="mbti" id="mbti" v-model.trim="mbti"><br>

      <input type="submit" value="회원가입">
    </form>
    <div v-if="showWarning" class="warning-modal">
      <div class="warning-content">
        <p>{{ warningMessage }}</p>
        <button @click="hideWarning">닫기</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const gender = ref(null)
const age = ref(null)
const nickname = ref(null)
const address = ref(null)
const salary = ref(null)
const money = ref(null)
const mbti = ref(null)

const userStore = useUserStore()
const showWarning = ref(false)
const warningMessage = ref('')

// 회원가입 함수
const signUp = function () {

  if (!username.value) {
    showWarning.value = true
    warningMessage.value = '아이디를 입력해주세요'
    return
  }
  if (!password1.value) {
    showWarning.value = true
    warningMessage.value = '비밀번호를 입력해주세요'
    return
  }
  if (password2.value !== password1.value) {
    showWarning.value = true
    warningMessage.value = '비밀번호가 일치하지 않습니다.'
    return
  }
  if (!gender.value) {
    showWarning.value = true
    warningMessage.value = '성별을 선택해주세요.'
    return
  }
  if (!address.value) {
    showWarning.value = true
    warningMessage.value = '주소를 입력해주세요.'
    return
  }

  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    gender: gender.value,
    age: age.value,
    address: address.value,
    salary: salary.value,
    money: money.value,
    mbti: mbti.value,
  }
  userStore.signUp(payload)
}

// 경고 메시지 숨기기
const hideWarning = function () {
  showWarning.value = false
}
</script>

<style scoped>
/* 가운데 정렬을 위한 스타일 */
.warning-modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.3);
}

.warning-content {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  text-align: center;
}
</style>