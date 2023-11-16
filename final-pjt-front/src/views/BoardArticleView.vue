<template>
  <div>
    <h1>게시판</h1>
    <RouterLink :to="{ name: 'board_create' }">
      [CREATE]
    </RouterLink>
    <BoardArticleList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useBoardStore } from '@/stores/board'
import { RouterLink } from 'vue-router'
import BoardArticleList from '@/components/BoardArticleList.vue'

const store = useBoardStore()

onMounted(() => {
  store.getBoardArticles()
})

</script>

<style>

</style>
