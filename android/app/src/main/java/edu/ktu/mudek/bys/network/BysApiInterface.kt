package edu.ktu.mudek.bys.network

import edu.ktu.mudek.bys.models.*
import retrofit2.Call
import retrofit2.http.*

interface BysApiInterface {
    @GET("users/?format=json")
    fun getUsers(): Call<ArrayList<Users>>

    @GET("users/{id}/?format=json")
    fun getUserDetails(@Path(
            "id") id: Int): Call<UserDetails>

    @GET("lessons/?format=json")
    fun getLessons(): Call<ArrayList<Lessons>>

    @GET("lessons/{id}/?format=json")
    fun getLessonDetails(@Path(
            "id") id: Int): Call<LessonDetails>

    @GET("exams/?format=json")
    fun getExams(): Call<ArrayList<Exams>>

    @GET("exams/{id}/?format=json")
    fun getExamDetails(@Path(
            "id") id: Int): Call<ExamDetails>

    @GET("other-documents/?format=json")
    fun getOtherDocuments(): Call<ArrayList<OtherDocuments>>

    @GET("other-documents/{id}/?format=json")
    fun getOtherDocumentDetails(@Path(
            "id") id: Int): Call<OtherDocumentDetails>

    @GET("request-documents/?format=json")
    fun getRequestDocuments(): Call<ArrayList<RequestDocuments>>

    @GET("request-documents/{id}/?format=json")
    fun getRequestDocumentDetails(@Path(
            "id") id: Int): Call<RequestDocumentDetails>

    @POST("auth/login/?format=json")
    @FormUrlEncoded
    fun AuthLogin(
            @Field("password") password: String,
            @Field("email") email: String): Call<AuthLogin>

}