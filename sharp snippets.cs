
// Mongo
using MongoDB.Bson;
using MongoDB.Driver;
using MongoDB.Driver.Builders;
using MongoDB.Driver.GridFS;
using MongoDB.Driver.Linq;

    public void GetCinnamon()
    {
        
        // Connect to Mongo
        string connectionString = "mongodb://34.219.62.195:27017";
        var client = new MongoClient(connectionString);
        var server = client.GetServer();
        var database = server.GetDatabase("test");
        var playercollection = database.GetCollection<BsonDocument>("players");

        var whereClause15 = Query.And(
            Query.EQ("name", "Fobi")
        );
        BsonDocument query15 = playercollection.FindOne(whereClause15);
        if (query15 != null)
        {
            Debug.Log(query15);
            //query15["cubes"] = item1;
            //playercollection.Save(query15);
            itemcount1.text = query15["cubes"].ToString();
        }

            // IEnumerator Talkative(){
    //     var url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=ko&dt=t&q=this";
    //     var webRequest = UnityWebRequest.Get(url);
    //     yield return webRequest.SendWebRequest();

    //     string x = webRequest.downloadHandler.text.Split(",")[0].Split("\"")[1];
    //     print(x);
    //     workLabel.text = x;
    // }

       
        foreach (var document in playercollection.Find(new QueryDocument("name", "Fobi")))
        {
            Debug.Log("6. SELECT DOC WHERE: \n" + document);
            if (document["cubes"]!=null)
            {
                scorestring.text = document["cubes"].ToString();
            }
        }
       
    }

// Request Get
using UnityEngine.Networking;
       IEnumerator GetRequest(string uri)
    {
        using (UnityWebRequest webRequest = UnityWebRequest.Get(uri))
        {
            // Request and wait for the desired page.
            yield return webRequest.SendWebRequest();

            string[] pages = uri.Split('/');
            int page = pages.Length - 1;

            if (webRequest.isNetworkError)
            {
                Debug.Log(pages[page] + ": Error: " + webRequest.error);
            }
            else
            {
                Debug.Log(pages[page] + ":\nReceived: " + webRequest.downloadHandler.text);
                //scorestring.text = webRequest.downloadHandler.text;
            }
        }
    }


//  World of Goo Attach
void Attach()
    {
        Collider[] hits = Physics.OverlapSphere(transform.position, 5);
        foreach(Collider hit in hits)
        {
            if (hit.tag == "Sphere")
            {
                float distance = Vector3.Distance(hit.transform.position, transform.position);
                if (distance < 5f)
                {
                    lines.enabled = true;
                    lines.SetPosition(0, transform.position);
                    lines.SetPosition(1, hit.transform.position);
                    lines.widthMultiplier = 1 - (distance / 10);
                }
                else
                {
                    lines.enabled = false;
                }
            }
        }
    }