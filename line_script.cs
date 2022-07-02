using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class line_script : MonoBehaviour
{
    LineRenderer linerenderer;

    public Transform origin;
    public Transform destin; //destination



    // Start is called before the first frame update
    void Start()
    {
        linerenderer = GetComponent<LineRenderer>();
        linerenderer.startWidth = 0.1f;
        linerenderer.endWidth = 0.1f;
        
    }

    // Update is called once per frame
    void Update()
    {
        linerenderer.SetPosition(0,origin.position);
        linerenderer.SetPosition(1,destin.position);
    }
}
