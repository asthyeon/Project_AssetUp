<template>
  <div>
    <h3 @click="goBack">[Back]</h3>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <div>
        <label for="title">제목 : </label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용 : </label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useArticleStore } from '@/stores/article'
import { useRouter } from 'vue-router'

const title = ref(null)
const content = ref(null)
const store = useArticleStore()
const router = useRouter()

// 게시글 작성 함수
const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
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
      store.getArticles()
      router.push({ name: 'articles' })
    })
    .catch((err) => {
      console.log(err.response.data)
    })
}

// 뒤로 가기
const goBack = function () {
  router.back()
}



</script>

<style>

</style>
