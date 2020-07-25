<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
        <h1 class="text-center">Vue Flask Library</h1>
        <hr />
        <br />
        <div class="text-center">
          <button type="button" class="btn btn-primary btn-sm" v-b-modal.book-modal>Add Book</button>
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
              <th scope="col">Read?</th>
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
                <span v-if="book.read">Yes</span>
                <span v-else>No</span>
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
    <!-- Modal Start -->
    <b-modal ref="addBookModal" id="book-modal" title="Add a new book" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-title-group" label="Title:" label-for="form-title-input">
          <b-form-input
            id="form-title-input"
            type="text"
            v-model="addBookForm.title"
            required
            placeholder="Enter title"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group" label="Author:" label-for="form-author-input">
          <b-form-input
            id="form-author-input"
            type="text"
            v-model="addBookForm.author"
            required
            placeholder="Enter author"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-rating-group" label="rating:" label-for="form-rating-input">
          <b-form-input
            id="form-rating-input"
            type="text"
            v-model="addBookForm.rating"
            required
            placeholder="Enter Rating"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addBookForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <!-- MOdal End -->
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      books: [],
      addBookForm: {
        title: '',
        author: '',
        rating: 0,
        read: []
      }
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
          // eslint-disable-next-line
          console.error(error)
        })
    },
    addBook(payload) {
      const path = 'http://localhost:5000/books'
      axios
        .post(path, payload)
        .then(() => {
          this.getBooks()
        })
        .catch(error => {
          // eslint-disable-next-line
          console.log(error)
          this.getBooks()
        })
    },
    initForm() {
      this.addBookForm.title = ''
      this.addBookForm.author = ''
      this.addBookForm.rating = 0
      this.addBookForm.read = []
    },
    onSubmit(evt) {
      evt.preventDefault()
      this.$refs.addBookModal.hide()
      let read = false
      if (this.addBookForm.read[0]) read = true
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        rating: this.addBookForm.rating,
        read // property shorthand
      }
      this.addBook(payload)
      this.initForm()
    },
    onReset(evt) {
      evt.preventDefault()
      this.$refs.addBookModal.hide()
      this.initForm()
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
