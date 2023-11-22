<template>
  <div>
    <h3 @click="goBack">[Back]</h3>
    <h1>게시글 수정</h1>
    <hr>
    <form @submit.prevent="updateArticle">
      <div>
        <label for="title">제목 : </label>
        <input v-model="updatedArticle.title" type="text" id="title" required />
      </div>
      <div>
        <label for="content">내용 : </label>
        <textarea v-model="updatedArticle.content" id="content" required></textarea>
      </div>
      <button type="submit">수정</button>
    </form>
    <hr>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted, watch } from 'vue'
import { useArticleStore } from '@/stores/article'
import { useUserStore } from '@/stores/user'
import { useRouter, useRoute } from 'vue-router'

const store = useArticleStore()
const userStore = useUserStore()
const route = useRoute()
const router = useRouter()
const updatedArticle = ref({ title: '', content: '' })

// 게시글 내용 불러오기
onMounted(() => {
  store.getArticleDetail(route.params.article_id)
})

watch(() => store.articleDetail, (val) => {
  updatedArticle.value.title = val.title
  updatedArticle.value.content = val.content
})

// 게시글 수정 함수
const updateArticle = function () {
  axios({
    method: 'put',
    url: `${store.API_URL}/api/v1/articles/${route.params.article_id}/`,
    data: updatedArticle.value,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then((res) => {
      console.log(res.data)
      router.push({ name: 'article_detail', params: { id: route.params.article_id } })
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

<style scoped>


</style>