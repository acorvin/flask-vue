<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
        <h1 class="text-center">Vue Flask Library</h1>
        <hr />
        <br />
        <div class="text-center">
          <button type="button" class="btn btn-primary btn-sm">Add Book</button>
        </div>
        <br />
        <div class="input-group mb-3">
          <input
            type="text"
            class="form-control"
            placeholder="Enter title, author, or rating"
            aria-label="Search"
            aria-describedby="button-addon2"
          />
          <div class="input-group-append">
            <button class="btn btn-outline-secondary" type="button" id="button-addon2">Search</button>
          </div>
        </div>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Rating</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <!-- Placeholder Data -->
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>{{ book.rating }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-primary btn-sm">Update</button>
                  <button type="button" class="btn btn-info btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      books: []
    }
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/books'
      axios
        .get(path)
        .then(res => {
          this.books = res.data.books
        })
        .catch(error => {
          console.error(error)
        })
    }
  },
  created() {
    this.getBooks()
  }
}
</script>

<style>
body {
  font-family: Arial;
  color: #f1faee;
  background-color: #1d3557;
}
td,
th,
h1 {
  color: #f1faee;
}

.btn {
  margin-right: 10px;
}
.btn-info {
  background-color: #e63946 !important;
  border: none;
}
.btn-primary {
  background-color: #457b9d !important;
  border: none;
}
.btn-outline-secondary {
  border-color: #f1faee !important;
  color: #f1faee;
}
</style>
