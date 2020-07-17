<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
        <h1 class="text-center">Vue Flask Library</h1>
        <hr />
        <br />
        <div class="text-center">
          <button type="button" class="btn btn-primary btn-sm">
            Add Book
          </button>
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
            <button
              class="btn btn-outline-secondary"
              type="button"
              id="button-addon2"
            >
              Search
            </button>
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
            <tr>
              <!-- Placeholder Data -->
              <td>The Witcher: Blood of Elves</td>
              <td>Andrzej Sapkowski</td>
              <td>94</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-primary btn-sm">
                    Update
                  </button>
                  <button type="button" class="btn btn-info btn-sm">
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<style>
.btn {
  margin-right: 10px;
}
</style>
