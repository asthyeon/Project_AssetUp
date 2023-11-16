<template>
  <div>
    <h3>전체 글</h3>
    <BoardArticleListItem
      v-for="board_article in store.board_articles"
      :key="board_article.id"
      :board_article="board_article"
    />
  </div>
</template>

<script setup>
import { useBoardStore } from '@/stores/board'
import BoardArticleListItem from '@/components/BoardArticleListItem.vue'

const store = useBoardStore()
console.log(store.board_articles)
</script>
