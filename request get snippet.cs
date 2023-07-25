using UnityEngine;
using UnityEngine.UI;
using System.Collections;
using UnityEngine.Networking;

public class GameController : MonoBehaviour
{
	public Text scorestring;
    public Text timer;
    public GameObject NPC;

    bool match;
	public int choice;

    void Start()
    {
        //StartCoroutine(GetRequest("http://34.219.62.195:5054/"));
        SetupPlayers(Random.Range(500,900));
    }

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
                scorestring.text = webRequest.downloadHandler.text;
            }
        }
    }
}
