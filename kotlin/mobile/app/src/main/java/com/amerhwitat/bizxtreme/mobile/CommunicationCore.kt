package com.amerhwitat.bizxtreme.mobile

import android.Manifest
import android.content.Context
import android.content.pm.PackageManager
import android.media.AudioAttributes
import android.media.AudioFormat
import android.media.AudioRecord
import android.media.AudioTrack
import android.media.MediaRecorder
import android.hardware.camera2.CameraManager
import androidx.core.content.ContextCompat
import java.security.MessageDigest
import java.util.concurrent.ConcurrentHashMap

data class ChatEvent(val conversationId:String,val senderId:String,val sequence:Long,val text:String,val sha256:String)
object ConversationSync { private val seen=ConcurrentHashMap<String,Long>(); fun accept(e:ChatEvent):Boolean { val h=MessageDigest.getInstance("SHA-256").digest(e.text.toByteArray()).joinToString(""){ "%02x".format(it) }; if(h!=e.sha256)return false; val k="${e.conversationId}:${e.senderId}"; val old=seen[k]?:-1L; if(e.sequence<=old)return false; seen[k]=e.sequence; return true } }
data class MediaCapabilities(val microphone:Boolean,val speaker:Boolean,val camera:Boolean){ companion object{fun detect(c:Context):MediaCapabilities{val mic=ContextCompat.checkSelfPermission(c,Manifest.permission.RECORD_AUDIO)==PackageManager.PERMISSION_GRANTED; val cam=ContextCompat.checkSelfPermission(c,Manifest.permission.CAMERA)==PackageManager.PERMISSION_GRANTED; val cm=c.getSystemService(Context.CAMERA_SERVICE) as CameraManager; val has=try{cm.cameraIdList.isNotEmpty()}catch(_:Exception){false}; return MediaCapabilities(mic,c.getSystemService(Context.AUDIO_SERVICE)!=null,cam&&has)}}}
class PcmVoiceEngine{private var r:AudioRecord?=null;private var p:AudioTrack?=null;fun start(rate:Int=48000){val n=AudioRecord.getMinBufferSize(rate,AudioFormat.CHANNEL_IN_MONO,AudioFormat.ENCODING_PCM_16BIT);r=AudioRecord(MediaRecorder.AudioSource.VOICE_COMMUNICATION,rate,AudioFormat.CHANNEL_IN_MONO,AudioFormat.ENCODING_PCM_16BIT,n);p=AudioTrack.Builder().setAudioAttributes(AudioAttributes.Builder().setUsage(AudioAttributes.USAGE_VOICE_COMMUNICATION).setContentType(AudioAttributes.CONTENT_TYPE_SPEECH).build()).setAudioFormat(AudioFormat.Builder().setSampleRate(rate).setEncoding(AudioFormat.ENCODING_PCM_16BIT).setChannelMask(AudioFormat.CHANNEL_OUT_MONO).build()).setBufferSizeInBytes(n).build();r?.startRecording();p?.play()};fun stop(){r?.stop();r?.release();r=null;p?.stop();p?.release();p=null}}
interface RealtimeMediaTransport{fun sendAudio(frame:ByteArray);fun sendVideo(frame:ByteArray);fun close()}
