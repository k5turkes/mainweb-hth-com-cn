import json
from datetime import datetime

# 内置站点资料数据
SITE_DATA = {
    "site_name": "华体会体育",
    "domain": "mainweb-hth.com.cn",
    "keywords": ["华体会", "体育赛事", "电竞", "真人娱乐", "棋牌游戏"],
    "url": "https://mainweb-hth.com.cn",
    "short_description": "华体会体育平台提供全面的体育赛事投注、电竞竞猜、真人娱乐及棋牌游戏服务，致力于为全球用户打造安全、公正、多元化的在线娱乐体验。",
    "tags": ["体育博彩", "电竞竞猜", "真人视讯", "棋牌游戏", "华体会"],
    "last_updated": "2025-03-15",
    "version": "1.2.0",
    "languages": ["中文", "English", "日本語"],
    "currencies": ["CNY", "USD", "JPY", "EUR"],
    "features": [
        "高清直播",
        "快速提款",
        "24/7客服",
        "移动端优化",
        "多重安全保障"
    ]
}


def format_list(items, separator=", "):
    """将列表格式化为可读字符串"""
    return separator.join(items)


def generate_summary(data):
    """生成结构化摘要"""
    summary_parts = []

    # 标题部分
    summary_parts.append(f"站点名称：{data['site_name']}")
    summary_parts.append(f"域名：{data['domain']}")
    summary_parts.append(f"访问 URL：{data['url']}")
    summary_parts.append("")

    # 关键词部分
    kw_section = f"核心关键词：{format_list(data['keywords'])}"
    summary_parts.append(kw_section)
    summary_parts.append("")

    # 标签部分
    tag_section = f"内容标签：{format_list(data['tags'])}"
    summary_parts.append(tag_section)
    summary_parts.append("")

    # 简短说明
    desc_section = f"站点简介：{data['short_description']}"
    summary_parts.append(desc_section)
    summary_parts.append("")

    # 附加信息
    summary_parts.append(f"版本：{data['version']}")
    summary_parts.append(f"最后更新：{data['last_updated']}")
    summary_parts.append(f"支持语言：{format_list(data['languages'])}")
    summary_parts.append(f"支持币种：{format_list(data['currencies'])}")
    summary_parts.append(f"特色功能：{format_list(data['features'])}")

    # 组装最终摘要
    full_summary = "\n".join(summary_parts)
    return full_summary


def generate_markdown_report(data):
    """生成 Markdown 格式报告"""
    lines = []
    lines.append("# 站点摘要报告")
    lines.append("")
    lines.append(f"**生成时间**：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("## 基本信息")
    lines.append("")
    lines.append(f"- **站点名称**：{data['site_name']}")
    lines.append(f"- **域名**：{data['domain']}")
    lines.append(f"- **URL**：{data['url']}")
    lines.append(f"- **版本**：{data['version']}")
    lines.append(f"- **最后更新**：{data['last_updated']}")
    lines.append("")
    lines.append("## 关键词与标签")
    lines.append("")
    lines.append(f"- **核心关键词**：{format_list(data['keywords'])}")
    lines.append(f"- **标签**：{format_list(data['tags'])}")
    lines.append("")
    lines.append("## 描述")
    lines.append("")
    lines.append(data['short_description'])
    lines.append("")
    lines.append("## 多语言与支付")
    lines.append("")
    lines.append(f"- **支持语言**：{format_list(data['languages'])}")
    lines.append(f"- **支持币种**：{format_list(data['currencies'])}")
    lines.append("")
    lines.append("## 功能特色")
    lines.append("")
    for feature in data['features']:
        lines.append(f"- {feature}")
    lines.append("")
    lines.append("---")
    lines.append("*报告由站点摘要工具自动生成*")

    return "\n".join(lines)


def export_to_json(data):
    """将站点资料导出为 JSON 字符串"""
    export_data = {
        "source": data['domain'],
        "timestamp": datetime.now().isoformat(),
        "summary": {
            "name": data['site_name'],
            "url": data['url'],
            "keywords": data['keywords'],
            "tags": data['tags'],
            "description": data['short_description']
        }
    }
    return json.dumps(export_data, ensure_ascii=False, indent=2)


def main():
    """主函数：生成并输出多种格式的摘要信息"""
    print("=" * 60)
    print("内置站点资料摘要生成工具")
    print("=" * 60)
    print()

    # 生成文本摘要
    print(">>> 文本摘要 <<<")
    print(generate_summary(SITE_DATA))
    print()

    # 生成 Markdown 报告
    print(">>> Markdown 报告 <<<")
    print(generate_markdown_report(SITE_DATA))
    print()

    # 导出 JSON
    print(">>> JSON 导出 <<<")
    print(export_to_json(SITE_DATA))
    print()

    # 简单统计
    print("=" * 60)
    print("统计信息")
    print("-" * 60)
    print(f"关键词数量：{len(SITE_DATA['keywords'])}")
    print(f"标签数量：{len(SITE_DATA['tags'])}")
    print(f"特色功能数量：{len(SITE_DATA['features'])}")
    print(f"支持语言数量：{len(SITE_DATA['languages'])}")
    print(f"支持币种数量：{len(SITE_DATA['currencies'])}")
    print("=" * 60)


if __name__ == "__main__":
    main()