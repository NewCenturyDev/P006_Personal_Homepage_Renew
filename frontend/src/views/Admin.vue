<template>
  <div class="admin">
    <v-md-editor class="editor" mode="editable" v-model="text" @upload-image="handleUploadImage" height="400px"></v-md-editor>
    <el-button v-on:click="check">테스트</el-button>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Admin',
  data() {
    return {
      text: '',
    };
  },
  methods: {
    check() {
      //eslint-disable-next-line
      console.log(this.text);
    },
    handleUploadImage(event, insertImage, files) {
      // Get the files and upload them to the file server, then insert the corresponding content into the editor
      console.log(files);

      // Here is just an example
      insertImage({
        url:
          '',
        desc: 'desc',
      });
    },
  }
}
</script>

<style lang="scss" scoped>
.admin {
  .editor {
    text-align: left;
  }
}
</style>
