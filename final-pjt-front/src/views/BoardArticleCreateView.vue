<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createBoardArticle">
      <div>
        <label for="title">제목:</label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용:</label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useBoardStore } from '@/stores/board'
import { useRouter } from 'vue-router'

const title = ref(null)
const content = ref(null)
const store = useBoardStore()
const router = useRouter()

// 게시글 작성 함수
const createBoardArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/board-articles/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      // console.log(res)
      router.push({ name: 'board' })
    })
    .catch((err) => {
      console.log(err.response.data)
    })
}



</script>

<style>

</style>
