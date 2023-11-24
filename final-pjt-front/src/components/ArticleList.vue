<template>
  <div>
    <h3>전체 글</h3>
    <hr>
    <ArticleListItem
      v-for="(article, index) in revesedArticles"
      :key="article.id"
      :article="article"
      :index="store.articles.length - index"
    />
  </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/article'
import ArticleListItem from '@/components/ArticleListItem.vue'
import { computed } from 'vue';

const store = useArticleStore()
console.log(store.articles)

const revesedArticles = computed(() => {
  return store.articles.slice().reverse()
})


</script>
