# PCA exercise, with some github practice

This exercise is for you to:

- finish the PCA exercise;
- practice Github collaborative workflow;
- see pull requests in action.

You're going to fork a repository, finish the PCA exercise, and then make a
pull request to the repository.  I'll review your pull request and merge it
when it is ready.

I've made private repositories for each of you for the exercise.  This will be
the "upstream" repository that you will fork, and make a pull request to.

- Make sure you have logged into your Github account;

- Go to the [course github organization] page.  You should see a private
  repository with a name like `yourname-pca-exercise` where `yourname` is
  your first name.

- Click on this repository;

- Fork the repository to your own account by clicking the "Fork" button
  towards the top left hand corner.  Your browser should then open a page
  pointing to your fork of the repository;

- Click the green "Clone or download" button and copy the URL to clone the
  forked repository;

- From the terminal, run `git clone
  https://github.com/your-gh-user/yourname-pca-exercise.git` where the URL is
  the URL of your cloned repository;

- Change directory into your new cloned repository:

  ```
  cd yourname-pca-exercise
  ```

- Make a new branch to work on, and checkout this new branch:

  ```
  git branch pca-exercise
  git checkout pca-exercise
  ```

- Finish the PCA exercise by filling in `pca_code.py`.  I suggest you keep
  the exercise web-page open in your browser, and work in IPython as in:

  ```bash
  $ ipython
  Python 3.5.2 (default, Jul 28 2016, 21:28:00)
  Type "copyright", "credits" or "license" for more information.

  IPython 5.1.0 -- An enhanced Interactive Python.
  ?         -> Introduction and overview of IPython's features.
  %quickref -> Quick reference.
  help      -> Python's own help system.
  object?   -> Details about 'object', use 'object??' for extra details.

  In [1]: %matplotlib
  Using matplotlib backend: MacOSX

  In [2]: run pca_code.py

  In [3]: plt.show()
  ```

- When you've finished:

  ```
  git add pca_code.py
  git commit
  ```

  and fill in a message describing the commit;

- Push these changes to your own repository, giving the branch name that you
  have been working on:

  ```
  git push origin pca-exercise --set-upstream
  ```

- Go back to the web page for your forked repository - the URL will be
  something like: <https://github.com/your-gh-user/yourname-pca-exercise>.
  Reload the page to make sure Github knows about your new branch;

- From the Branch list-box near the top-left of the page, select your new
  `pca-exercise` branch. Click on the `pca_code.py` file to check it is what
  you were expecting;

- Click on the "New pull request" button next to the branch name list-box.
  Type in a message to me, and click the green "Create pull request" button at
  the bottom.   When you do, I'll get an email that you've made a pull
  request;

- Now the fun begins.  I'll use the Github Pull request interface to comment
  on your code, to give you feedback, and make suggestions for changes.  This
  is a "code review";

- To make changes, go back to your repository, edit the code, and make a new
  commit with the changes.  When you finished making changes:

  ```
  git push
  ```

  to push back up to your Github fork, and `pca-exercise` branch.  The
  changes show up automatically in the Github Pull-request interface.

Happy hunting.
