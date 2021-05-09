from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(f"""

<title>secure authorize server</title>
<h1>i will be oauth2 server</h1>
<script>
    alert("come here later")
    document.location = "/index.php"
</script>


""")
