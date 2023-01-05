using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Windows.Speech;

public class VoiceInput : MonoBehaviour
{
    // Icons
    public Image mic;
    public Sprite[] micIcons;

    // Recognizer
    private KeywordRecognizer keywordRecognizer;
    private Dictionary<string, System.Action> keywords = new Dictionary<string, System.Action>();
    private List<string> words = new List<string>();
    private string currentWord;

    private void Awake()
    {
        Commands();
    }

    private void Start()
    {
        InitRecognizer();
    }

    private void FixedUpdate()
    {
        MicroPhoneIcon();
    }

    void MicroPhoneIcon()
    {
        Sprite current;
        if (keywordRecognizer.IsRunning)
        {
            current = micIcons[0];
        }
        else
        {
            current = micIcons[1];
        }

        mic.sprite = current;
    }

    void InitRecognizer()
    {
        if (keywordRecognizer == null)
        {
            keywordRecognizer = new KeywordRecognizer(keywords.Keys.ToArray(), ConfidenceLevel.Low);
            keywordRecognizer.OnPhraseRecognized += KeywordRecognizerOnPhraseRecognized;
        }
        if (!keywordRecognizer.IsRunning)
        {
            keywordRecognizer.Start();
        }
    }

    void Commands()
    {
        words.Add("walk to");
        words.Add("give");
        words.Add("open");
        words.Add("close");
        words.Add("pick up");
        words.Add("look at");
        words.Add("talk to");
        words.Add("use");
        words.Add("push");
        words.Add("pull");

        for (int i = 0; i < words.Count; i++)
        {
            keywords.Add(words[i], () =>
            {
                KeywordCalled();
            });
        }
    }

    void KeywordCalled()
    {
        print("You just said: " + currentWord);
    }

    void KeywordRecognizerOnPhraseRecognized(PhraseRecognizedEventArgs args)
    {
        System.Action keywordAction;

        if (keywords.TryGetValue(args.text, out keywordAction))
        {
            currentWord = args.text;
            keywordAction.Invoke();
        }

    }
}
