<template>
  <div>
    <h1>게시판</h1>
    <hr>
    <RouterLink :to="{ name: 'article_create' }">
      [CREATE]
    </RouterLink>
    
    <ArticleList v-if="store.articles"/>
    <p v-if="store.articles.length === 0">
      <h3>글이 없습니다.</h3>
    </p>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useArticleStore } from '@/stores/article'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useArticleStore()

onMounted(() => {
  console.log(store.articles);
  if (store.articles.length > 0) {
    store.getArticles()
  }
})

</script>

<style>

</style>
