package edu.ktu.mudek.bys.fragment

import android.os.Bundle
import android.support.v4.app.Fragment
import android.support.v7.widget.LinearLayoutManager
import android.support.v7.widget.RecyclerView
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.LinearLayout
import android.widget.Toast
import edu.ktu.mudek.R
import edu.ktu.mudek.R.layout.*
import edu.ktu.mudek.bys.adapters.LessonsAdapter
import edu.ktu.mudek.bys.models.Lessons
import edu.ktu.mudek.bys.network.BysApiClient
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response




class HomeFragment : Fragment(){
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {

        val rootView = inflater.inflate(fragment_home, container, false)
        val recyclerView = rootView.findViewById<RecyclerView>(R.id.recyclerView)

        recyclerView.layoutManager = LinearLayoutManager(activity?.baseContext, LinearLayout.VERTICAL, false)
        BysApiClient.instance.getLessons().enqueue(object: Callback<ArrayList<Lessons>>{

            override fun onResponse(call: Call<ArrayList<Lessons>>, response: Response<ArrayList<Lessons>>) {
                if (response.isSuccessful) {
                    Toast.makeText(activity?.baseContext, "... which is successful!", Toast.LENGTH_SHORT).show()
                    Log.i("Response",response.body().toString())
                    Log.i("Call",call.toString())
                    Log.i("Call",call.request().headers().toString())
                    Log.i("Call",call.request().body().toString())

                    val lessonsAdapter = LessonsAdapter(response.body()!!)
                    recyclerView.adapter = lessonsAdapter

                        lessonsAdapter.onItemClick= { Lessons ->

                            val fragment1 = LessonDetailsFragment()
                            val fragmentManager = fragmentManager
                            val fragmentTransaction = fragmentManager!!.beginTransaction()
                            fragmentTransaction.replace(R.id.relativelayout, fragment1)
                            fragmentTransaction.commit()
                        }

                }
                else {
                    Toast.makeText(activity?.baseContext, "... which is bad :(", Toast.LENGTH_SHORT).show()
                    Log.i("Response",response.body().toString())
                    Log.i("Call",call.toString())
                    Log.i("Call",call.request().headers().toString())
                    Log.i("Call",call.request().body().toString())
                }
            }

            override fun onFailure(call: Call<ArrayList<Lessons>>, t: Throwable) {
                Toast.makeText(activity?.baseContext,t.message,Toast.LENGTH_LONG).show()
                Log.i("Response","onFailure",t)
                Log.i("Call",call.toString())
                Log.i("Call",call.request().headers().toString())
                Log.i("Call",call.request().body().toString())

            }

        } )

        return rootView
    }
}
