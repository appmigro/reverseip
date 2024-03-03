# templates/_helpers.tpl
{{- define "reverseip-app.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name }}
{{- end -}}

{{- define "reverseip-app.name" -}}
{{- default "reverseip-app" .Chart.Name }}
{{- end -}}
