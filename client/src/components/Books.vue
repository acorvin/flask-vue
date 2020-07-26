<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
        <h1 class="text-center">Vue Flask Library</h1>
        <hr />
        <br />
        <alert :message="message" v-if="showMessage"></alert>
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
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                    type="button"
                    class="btn btn-primary btn-sm"
                    v-b-modal.book-update-modal
                    @click="editBook(book)"
                  >Update</button>
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="onDeleteBook(book)"
                  >Delete</button>
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
            <b-form-checkbox value="true">Have you read this book?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <!-- Modal End -->
    <!-- Update Modal Start -->
    <b-modal ref="editBookModal" id="book-update-modal" title="Update" hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-title-edit-group" label="Title:" label-for="form-title-edit-input">
          <b-form-input
            id="form-title-edit-input"
            type="text"
            v-model="editForm.title"
            required
            placeholder="Enter title"
          ></b-form-input>
        </b-form-group>
        <b-form-group
          id="form-author-edit-group"
          label="Author:"
          label-for="form-author-edit-input"
        >
          <b-form-input
            id="form-author-edit-input"
            type="text"
            v-model="editForm.author"
            required
            placeholder="Enter author"
          ></b-form-input>
          <b-form-input
            id="form-rating-edit-input"
            type="text"
            v-model="editForm.rating"
            required
            placeholder="Enter rating"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group v-model="editForm.read" id="form-checks">
            <b-form-checkbox value="true">Have you read this book?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <!-- Update Modal End -->
  </div>
</template>

<script>
import axios from 'axios'
import Alert from './Alert.vue'

export default {
  data() {
    return {
      books: [],
      addBookForm: {
        title: '',
        author: '',
        rating: 0,
        read: [],
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        title: '',
        author: '',
        rating: 0,
        read: [],
      },
    }
  },
  components: {
    alert: Alert,
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/books'
      axios
        .get(path)
        .then((res) => {
          this.books = res.data.books
        })
        .catch((error) => {
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
          this.message = 'Title added successfully'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error)
          this.getBooks()
        })
    },
    editBook(book) {
      this.editForm = book
    },
    removeBook(bookID) {
      const path = `http://localhost:5000/books/${bookID}`
      axios
        .delete(path)
        .then(() => {
          this.getBooks()
          this.message = 'Book removed!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
          this.getBooks()
        })
    },
    onDeleteBook(book) {
      this.removeBook(book.id)
    },
    initForm() {
      this.addBookForm.title = ''
      this.addBookForm.author = ''
      this.addBookForm.rating = 0
      this.addBookForm.read = []
      this.editForm.id = ''
      this.editForm.title = ''
      this.editForm.author = ''
      this.addForm.rating = 0
      this.editForm.read = []
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
        read, // property shorthand
      }
      this.addBook(payload)
      this.initForm()
    },
    onSubmitUpdate(evt) {
      evt.preventDefault()
      this.$refs.editBookModal.hide()
      let read = false
      if (this.editForm.read[0]) read = true
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        rating: this.editForm.rating,
        read,
      }
      this.updateBook(payload, this.editForm.id)
    },
    onReset(evt) {
      evt.preventDefault()
      this.$refs.addBookModal.hide()
      this.initForm()
    },
    onResetUpdate(evt) {
      evt.preventDefault()
      this.$refs.editBookModal.hide()
      this.initForm()
      this.getBooks() // why?
    },
  },
  created() {
    this.getBooks()
  },
  updateBook(payload, bookID) {
    const path = `http://localhost:5000/books/${bookID}`
    axios
      .put(path, payload)
      .then(() => {
        this.getBooks()
        this.message = 'Book updated!'
        this.showMessage = true
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error)
        this.getBooks()
      })
  },
}
</script>

<style>
body {
  font-family: Arial;
  color: #f1faee;
  background-color: #1d3557;
}
.modal-content {
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
