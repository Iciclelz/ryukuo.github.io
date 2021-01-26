project_name = input("Project Name: ")

text = """
<!DOCTYPE html>
<html>

    <head>
      <link href="https://ryukuo.github.io/styles.css" rel="stylesheet">
      <link href="https://ryukuo.github.io/semantic.css" rel="stylesheet">
      <link href="https://ryukuo.github.io/metro/css/metro.css" rel="stylesheet">
      <script src="https://ryukuo.github.io/jquery-2.2.3.js"></script>
      <script src="https://ryukuo.github.io/metro/js/metro.js"></script>
      <script src="https://ryukuo.github.io/semantic.js"></script>
      <title>
    """ + project_name + """
    </title>
    </head>

    <body>
      <script type="text/javascript">
        $(function () {
          $("#sidebar-content").load("https://ryukuo.github.io/sidebar.html");
        });
      </script>
      <div id="sidebar-content"></div>
      <div class='article' style="margin-left: 250px; margin-top: -1800px">
        <div style="background: url('https://ryukuo.github.io/background.jpg')">
          <br>
          <h1 class="ui header" style="margin-left: 50px; margin-top: 40px; margin-bottom: 40px; margin-right: 40px">
            <span>
    """ + project_name + """
    </span>
            <div class="sub header">
    """ + input("Project Sub: ") + """

    </div>
          </h1>
          <br>
          <hr>
        </div>
        <div class="main ui intro container" style="background: height: 1620px; margin-top: -10px">
          <br>
          <div class="ui existing segment" style="background: url('https://ryukuo.github.io/ryukuo-background.jpg'); margin-left: 50px; margin-top: 40px; margin-bottom: 40px; margin-right: 40px">
            <div class="example" data-text="intro">
            <p>

    """ + input("Project Intro: ") + """
      </p>
            </div>

            <div class="example" data-text="screenshot">
            <p><center><img src="
    """ + input("Screenshot: ") + """

    "></center></p>
            </div>


            <div class="example" data-text="update log">
    """ + input("Update Log (GIST LINK): ") + """
            </div>

            <center>
              <div class="example" data-text="download">
              <h1><span class="purple">downloads</span></h1>
              <a href="
    """ + input("Download URL: ") + """"><button class="button success block-shadow-success text-shadow">
    """ + project_name + " " + input("Version: ") + """
    </button>
              </a>
              </div>
            </center>
          </div>


          <br>
        </div>
      </div>
    </body>

    </html>"""

with open (project_name.replace(" ", "-") + ".html", 'w') as f:
    f.write(text)

print("Finished.")
