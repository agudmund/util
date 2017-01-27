using UnityEngine;
using System.Collections;

public class Cycle : MonoBehaviour {

    private DoStuff ctrl;

    // interval between beats
    public int cycle;

    // Total health
    public float energy;

    // Mutation variations
    public GameObject[] variations;

    // Time of Birth
    private float birth;

    private Color color;
    private int vibrancy = 0;

    void OnMouseDown()
    {
        if (energy < 10)
        {
            energy += 1;
            print("[" + gameObject.name + "][" + energy + "] Yum yum, thanks!");

        }
    }

    void set_ctrl()
    {
        GameObject gameControllerObject = GameObject.FindWithTag("GameController");
        if (gameControllerObject != null)
        {
            ctrl = gameControllerObject.GetComponent<DoStuff>();
        }
    }

    void Start()
    {
        
        energy = Random.Range(3,9);
        
        color = new Color(0, energy/10, 0);
        gameObject.GetComponent<Renderer>().material.color = color;

        set_ctrl();

        cycle = Random.Range(1, 7);
       
        birth = Time.time;
        StartCoroutine(Those());
    }

    IEnumerator Those()
    {
        // Do stuff every x seconds
        while (energy > 0)
        {
            yield return new WaitForSeconds(cycle);
            energy -= 1;
            
            Exist();
        }
        Destroy(gameObject);

    }

    void FixedUpdate()
    {
        if (color.g > 0)
        {
            gameObject.GetComponent<Renderer>().material.color = new Color(color.r, (energy / 10), color.b);
        }
    }

    void Exist()
    {
        int score = Random.Range(0, 10);
        Vector3 current = gameObject.transform.position;
        Vector3 targetcoord = new Vector3(current.x + Random.Range(-1, 2), 1, current.z + Random.Range(-1, 2));

        foreach (var n in ctrl.done)
        {
            if (targetcoord == n)
            {
                vibrancy += 100;
                gameObject.GetComponent<Renderer>().material.color = new Color(color.r, color.g, color.b*1.1f);
                gameObject.transform.localScale = gameObject.transform.localScale * 0.9f;
                return;
            }            
        }

        gameObject.GetComponent<Rigidbody>().AddForce(0, vibrancy, 0);

        if (score > 6 & score < 8)
        {
            GameObject target = Instantiate(gameObject, targetcoord, Quaternion.identity) as GameObject;
            print("[" + gameObject.name + "][" + energy + "] Look! It's a clone.");
            
        }
    }

}
