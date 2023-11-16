<template>
  <div>
    <h1>Detail</h1>
    <div v-if="board_article">
      <p>작성자 : {{ board_article.user_name }}</p>
      <p>제목 : {{ board_article.title }}</p>
      <p>내용 : {{ board_article.content }}</p>
      <p>작성일 : {{ board_article.created_at }}</p>
      <p>수정일 : {{ board_article.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useBoardStore } from '@/stores/board'
import { useRoute } from 'vue-router'

const store = useBoardStore()
const route = useRoute()
const board_article = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/board-articles/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      board_article.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

</script>

<style>

</style>
